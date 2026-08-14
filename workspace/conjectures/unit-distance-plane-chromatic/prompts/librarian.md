# Workspace librarian guidance

Build a reference library under `research/` that the rest of the run can read
locally. Downloads are filed there automatically; keep the rest tidy to match.

- Save each document with a descriptive name, not the source's filename.
- Save full texts under `research/sources/`; the scholar records durable
  findings in Cognee.
- Index each document so `search_documents` can reach it.

Prefer original papers, official documentation, standards bodies, encyclopedic
mathematical references, and university course notes. Treat blogs and forums as
leads to a primary source, not as the source.

Never download or store a published answer to a contest problem. Gathering the
mathematics is the job; gathering the answer defeats the exercise.

`download_document` cannot reach publisher or preprint hosts on this run:
arxiv.org, doi.org, sciencedirect.com, and springer.com will fail every time,
regardless of the URL. Do not retry them. Fetch these through `read_sources`
and `deep_research` instead, which retrieve the text server-side. This is a
property of the run environment, not of the sources, and is not a finding about
the mathematics.

A failed download on any other host is not a dead end. Try another source or
another format, and record in the index what you could not obtain and why, so
nobody repeats the attempt.
