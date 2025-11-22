import os
import subprocess
import sys
import shutil

def compile_latex(tex_file):
    tex_file = os.path.abspath(tex_file)
    tex_dir = os.path.dirname(tex_file)
    tex_name = os.path.basename(tex_file)

    # Find available engine
    engine = shutil.which("tectonic") or shutil.which("xelatex")
    if not engine:
        print("ERROR: No LaTeX engine found. Install 'tectonic' or 'xelatex'.")
        return

    print(f"Using engine: {engine}")
    print(f"Compiling: {tex_file}")

    if "tectonic" in engine:
        cmd = [engine, tex_file, "--keep-intermediates"]
    else:
        cmd = [engine, "-interaction=nonstopmode", "-halt-on-error", tex_name]

    result = subprocess.run(cmd, cwd=tex_dir)

    if result.returncode == 0:
        print("✔ PDF generated successfully!")
        print(f"Output: {os.path.join(tex_dir, 'input.pdf')}")
    else:
        print("❌ Compilation failed. Check your LaTeX for errors.")

if __name__ == "__main__":
    # If no file is given → default to resume.tex
    if len(sys.argv) < 2:
        filename = "resume.tex"
        print("No file given. Using default: resume.tex")
    else:
        filename = sys.argv[1]

    compile_latex(filename)
