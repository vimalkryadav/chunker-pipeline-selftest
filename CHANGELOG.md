# Changelog

## Unreleased

- `chunk()` now returns the trailing partial chunk when the sequence length is
  not a multiple of `size`, instead of dropping it.
