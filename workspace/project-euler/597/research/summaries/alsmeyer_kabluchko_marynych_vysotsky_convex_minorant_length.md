> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/alsmeyer_kabluchko_marynych_vysotsky_convex_minorant_length.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/2002.07687 | converted from PDF -->

Mind Your Weight(s): A Large-scale Study on Insufﬁcient
Machine Learning Model Protection in Mobile Apps

Zhichuang Sun
Northeastern University Ruimin Sun
Northeastern University Long Lu
Northeastern University

Alan Mislove
Northeastern University

Abstract

On-device machine learning (ML) is quickly gaining
popularity among mobile apps. It allows ofﬂine model
inference while preserving user privacy. However, ML models,
considered as core intellectual properties of model owners,
are now stored on billions of untrusted devices and subject to
potential thefts. Leaked models can cause both severe ﬁnancial
loss and security consequences.
This paper presents the ﬁrst empirical study of ML model
protection on mobile devices. Our study aims to answer three
open questions with quantitative evidence: How widely is
model protection used in apps? How robust are existing model
protection techniques? What impacts can (stolen) models in-
cur? To that end, we built a simple app analysis pipeline and an-
alyzed 46,753 popular apps collected from the US and Chinese
app markets. We identiﬁed 1,468 ML apps spanning all popular
app categories. We found that, alarmingly, 41% of ML apps do
not protect their models at all, which can be trivially stolen from
app packages. Even for those apps that use model protection
or encryption, we were able to extract the models from 66%
of them via unsophisticated dynamic analysis techniques. The
extracted models are mostly commercial products and used for
face recognition, liveness detection, ID/bank card recognition,
and malware detection. We quantitatively estimated the poten-
tial ﬁnancial and security impact of a leaked model, which can
amount to millions of dollars for different stakeholders.
Our study reveals that on-device models are currently at
high risk of being leaked; attackers are highly motivated to
steal such models. Drawn from our large-scale study, we report
our insights into this emerging security problem and discuss
the technical challenges, hoping to inspire future research on
robust and practical model protection for mobile devices.

1 Introduction

Mobile app developers have been quickly adopting on-device
machine learning (ML) techniques to provide artiﬁcial intelli-
gence (AI) features, such as facial recognition, augmented/vir-
tual reality, image processing, voice assistant, etc. This trend
 is now boosted by new AI chips available in the latest smart-
phones [1], such as Apple’s Bionic neural engine, Huawei’s
neural processing unit, and Qualcomm’s AI-optimized SoCs.
Compared to performing ML tasks in the cloud, on-device
ML (mostly model inference) offers unique beneﬁts desirable
for mobile users as well as app developers. For example,
it avoids sending (private) user data to the cloud and does
not require network connection. For app developers or
ML solution providers, on-device ML greatly reduces the
computation load on their servers.
On-device ML inference inevitably stores ML models
locally on user devices, which however creates a new security
challenge. Commercial ML models used in apps are often part
of the core intellectual property (IP) of vendors. Such models
may fall victim to theft or abuse, if not sufﬁciently protected.
In fact, on-device ML makes model protection much more
challenging than server-side ML because models are now
stored on user devices, which are fundamentally untrustworthy
and may leak models to curious or malicious parties.
The consequences of model leakage are quite severe.
First, with a leaked model goes away the R&D investment
of the model owner, which often includes human, data,
and computing costs. Second, when a proprietary model is
obtained by unethical competitors, the model owner loses the
competitive edge or pricing advantage for its products. Third,
a leaked model facilitates malicious actors to ﬁnd adversarial
inputs to bypass or confuse the ML systems, which can lead

*[excerpt ends; 88456 characters not shown — see `research/sources/alsmeyer_kabluchko_marynych_vysotsky_convex_minorant_length.full.md`]*
