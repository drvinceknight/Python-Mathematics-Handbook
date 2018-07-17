from invoke import task
import pathlib

@task
def main(c):
    """
    Render all ipynb files
    """
    path = pathlib.Path(".")
    ipynbs = path.glob("*ipynb")
    for p in ipynbs:
        print(p)
        tex = str(p.stem) + ".tex"
        c.run(f"jupyter-nbconvert --to latex {p}")
        c.run(f"latexmk --xelatex {tex}")
        c.run(f"latexmk -c")

@task
def test(c):
    """
    Test all the notebook outputs
    """
    c.run("pytest --nbval --current-env")
