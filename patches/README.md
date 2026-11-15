# patches/

**English** | [Español](README.es.md)

Diffs of our v1 Home changes against the pinned upstream commit, so this repo
stays free of vendored upstream code.

- `001-v1-tu7125-home.patch` — vs `GuillemCortesOvide/hack-tv@f52b545`:
  service/widget filter + name dedup, sports tray (`DAZN`, `Orange`) with
  tolerant matching, `showAll` flag (rest hidden), second-row no-scroll,
  tightened header, square icon, real DAZN/Orange tiles, installer asset list.
  No secrets inside (audited: no IPs, DUIDs, MACs, tokens, certs).

Apply on a fresh clone:

```powershell
git checkout f52b5450d9c3bec7e935d6a395ffdad8bf9cef
git apply <path-to>/001-v1-tu7125-home.patch
```
