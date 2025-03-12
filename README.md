# All ✅, no ❌ - Intro to `pytest`

Writing code for research often feels more like a creative process than a software engineering effort. Best practices from software engineering can, however, make your code more robust, reliable, easier to read and reproduce. One such practice is unit testing: Writing and running tests for your code that ensure the intended behavior.

PyTest is a popular framework for unit testing in Python that lets you write simple, unintrusive tests with very little additional code. In this workshop, we will go over the basics of testing with PyTest, introduce Test-Driven Development, and show you how to make sure your code checks all the boxes.

Advanced beginners in Python will most likely get the most out of this session, but programmers of all languages and experience levels are welcome.


## Getting started

### Requirements

Basic knowledge of Python will be helpful, but no prior web development experience is necessary—just bring your laptop and a willingness to learn!

The requirements for the Python code can be installed using the following command:

```
pip install .
```

If you use [uv](https://docs.astral.sh/uv/), you can instead run:

```
uv sync
```

### Usage

The repo has the following structure:

- `ppt`: The slide deck used in the introduction
- `src`: Python scripts illustrating the main concepts discussed in this workshop

### Running the tests

To run all tests, simply run:

```
pytest
```

There many command line options available, for example to run individual tests or increase the verbosity. For more info, check out the [pytest documentation](https://docs.pytest.org/).


## Issues and feedback

If you run into any trouble working with these materials, have some questions about the content, or want to give general feedback, feel free to go through one of these channels to get in touch with us:

- [Open a new issue](https://github.com/Simon-Stone/intro-to-pytest/issues)
- [Send an email](mailto:simon.stone@dartmouth.edu)
- [Schedule a meeting](https://calendly.com/simon-stone-dartmouth) (Dartmouth-members only)

## Licensing

<table>
<tbody>
  <tr>
    <td style="padding:0px;border-width:0px;vertical-align:center">
    Instructional materials created by Simon Stone for Dartmouth College under <a href="https://creativecommons.org/licenses/by/4.0/">Creative Commons CC BY-NC 4.0 License</a>.
    </td>
    <td style="padding:0 0 0 1em;border-width:0px;vertical-align:center"><img alt="Creative Commons License" src="https://i.creativecommons.org/l/by/4.0/88x31.png"/></td>
  </tr>
</tbody>
</table>

Except where otherwise noted, the example programs are made available under the OSI-approved MIT license.