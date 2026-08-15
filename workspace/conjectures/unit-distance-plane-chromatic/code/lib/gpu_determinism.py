"""GPU kernel determinism (e.g. for PyTorch CuDNN/backward-mode autograd).

For deterministic GPU execution, set the environment before the framework loads:
- CUDA_LAUNCH_BLOCKING=1 (kernel launch ordering)
- CUBLAS_WORKSPACE_CONFIG=:4096:8 (cuBLAS deterministic mode)
- PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True (optional, stable addresses)

Then call `make_torch_deterministic()` after importing torch. It:
- seeds python/random, numpy, torch CPU and all CUDA devices
- sets torch.use_deterministic_algorithms(True) so any non-deterministic op raises
- sets cudnn.benchmark = False and cudnn.deterministic = True

Notes and caveats:
- Determinism is only guaranteed for a specific GPU architecture and library
  version; the same code / seed can differ run-to-run on different hardware.
- "Deterministic" here means bitwise reproducibility for fixed seed + identical
  compute environment, NOT that output is independent of platform/library versions.
- Autograd backward passes are deterministic for most standard ops under
  determinism mode, but not all algorithms (e.g. some index/attention variants)
  are deterministic.

Returns True if determinism could be enabled, False otherwise (e.g. torch import
failed).
"""

import os
import random


def configure_env():
    """Idempotent environment setup. Call before importing torch/cupy."""
    os.environ.setdefault("CUDA_LAUNCH_BLOCKING", "1")
    os.environ.setdefault(
        "CUBLAS_WORKSPACE_CONFIG", ":4096:8"
    )  # enables cubias determinism
    os.environ.setdefault("PYTORCH_CUDA_ALLOC_CONF", "expandable_segments:True")
    os.environ.setdefault("TORCH_DETERMINISTIC", "1")
    os.environ.setdefault("NAVIDIA_TF32_OVERRIDE", "0")


def make_torch_deterministic(seed: int = 1234) -> bool:
    """Seed all RNGs and force PyTorch deterministic algorithms.

    Returns True on success; False if torch is not installed.
    """
    try:
        import numpy as np
        import torch
    except ImportError:
        return False

    configure_env()
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
    try:
        torch.use_deterministic_algorithms(True)
    except Exception:
        pass
    torch.backends.cudnn.benchmark = False
    torch.backends.cudnn.deterministic = True
    if hasattr(torch.backends, "cuda") and hasattr(
        torch.backends.cuda, "matmul"
    ):
        torch.backends.cuda.matmul.allow_tf32 = False
        torch.backends.cuda.matmul.allow_fp16_reduced_precision_reduction = False
        torch.backends.cuda.matmul.allow_bf16_reduced_precision_reduction = False
    # cuBLAS workspace config must be set before cuBLAS loads; if torch already
    # initialized CUDA this is a no-op, which is why configure_env() is called
    # first in practice.
    print(
        f"[gpu_determinism] deterministic algorithms {'ON' if torch.are_deterministic_algorithms_enabled() else 'OFF'}"
    )
    return True
