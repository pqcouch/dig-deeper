#!/usr/bin/env python3
"""Stamp a bundled copy of the canonical house .odt converter, or check one for drift.

  python3 bundle_converter.py <destination.py>     write a stamped copy
  python3 bundle_converter.py --check <file.py>    report whether a copy is current

Why this exists. Two converters existed in this toolkit and they diverged
silently: `point-purpose/scripts/render_odt.py` was written independently, and
walked into all four of the traps `make_odt.py` had to be fixed for (no font-face
declaration for the house font, complex-script size not raised, content.xml never
patched, no `---` pre-flight and no section-count verification). A copy that is
GENERATED and hash-stamped makes that divergence visible instead of silent.
"""
import hashlib, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
CANON = HERE / "make_odt.py"

def body_and_version():
    src = CANON.read_text(encoding="utf-8")
    m = re.search(r'^HOUSE_ODT_VERSION = "([^"]+)"', src, re.M)
    if not m:
        sys.exit("canonical converter carries no HOUSE_ODT_VERSION")
    return src, m.group(1), hashlib.sha256(src.encode("utf-8")).hexdigest()

def header(version, digest):
    return ("# GENERATED COPY - DO NOT EDIT.\n"
            "# Source:  _house-style/make_odt.py\n"
            "# Version: %s\n"
            "# sha256:  %s\n"
            "# Regenerate: python3 _house-style/bundle_converter.py <this file>\n"
            "# Check:      python3 _house-style/bundle_converter.py --check <this file>\n"
            "# Edit the canonical file, bump its version, then regenerate every copy.\n\n"
            % (version, digest))

def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    src, version, digest = body_and_version()
    if args[0] == "--check":
        if len(args) < 2:
            sys.exit("--check needs a file")
        p = pathlib.Path(args[1])
        if not p.exists():
            sys.exit("missing: %s" % p)
        t = p.read_text(encoding="utf-8")
        mv = re.search(r'^# Version: (\S+)', t, re.M)
        mh = re.search(r'^# sha256:  (\S+)', t, re.M)
        if not (mv and mh):
            print("NOT A GENERATED COPY  %s - it carries no stamp, so it cannot be checked" % p)
            return 2
        # Two independent failures, and they need separate answers:
        #   the copy was edited by hand   -> its body no longer matches its own stamp
        #   the canonical file moved on   -> its stamp no longer matches the canonical hash
        body = t.split("\n\n", 1)[1] if "\n\n" in t else ""
        body_digest = hashlib.sha256(body.encode("utf-8")).hexdigest()
        edited = body_digest != mh.group(1)
        stale = mh.group(1) != digest
        if edited:
            print("EDITED BY HAND  %s\n   its body does not match the stamp it carries."
                  "\n   Put the change in _house-style/make_odt.py, bump the version, regenerate." % p)
        if stale:
            print("STALE  %s\n   copy is version %s (sha %s)\n   canonical is version %s (sha %s)"
                  % (p, mv.group(1), mh.group(1)[:16], version, digest[:16]))
        if edited or stale:
            return 1
        print("CURRENT  %s  (version %s)" % (p, mv.group(1)))
        return 0
    dest = pathlib.Path(args[0])
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(header(version, digest) + src, encoding="utf-8")
    print("wrote %s  (version %s)" % (dest, version))
    return 0

if __name__ == "__main__":
    sys.exit(main())
