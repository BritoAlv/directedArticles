from mkdocs.plugins import BasePlugin


class MathBlockPlugin(BasePlugin):
    config_scheme = ()

    def on_page_markdown(self, markdown, page, config, files):
        lines = markdown.split("\n")
        out = []
        in_fence = False
        in_block = False
        n = len(lines)
        for i, line in enumerate(lines):
            s = line.lstrip()
            indent = line[: len(line) - len(s)]
            if s.startswith("```") or s.startswith("~~~"):
                in_fence = not in_fence
                out.append(line)
                continue
            if in_fence or len(indent) >= 4:
                out.append(line)
                continue
            prev_blank = i == 0 or not lines[i - 1].strip()
            nxt = lines[i + 1] if i + 1 < n else ""
            if in_block:
                if s.startswith("$$") or s.endswith("$$"):
                    in_block = False
                    out.append(line)
                    if nxt.strip() and not nxt.lstrip().startswith("$$"):
                        out.append("")
                else:
                    out.append(line)
                continue
            if s.startswith("$$"):
                opens = s == "$$" or not s.endswith("$$")
                if not prev_blank:
                    out.append("")
                out.append(line)
                if opens:
                    in_block = True
                elif nxt.strip() and not nxt.lstrip().startswith("$$"):
                    out.append("")
                continue
            out.append(line)
        return "\n".join(out)
