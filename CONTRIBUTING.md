# Contributing

We love pull requests from everyone.

1. Fork, then clone the repo:

       git clone git@github.com:your-username/pyMG.git

2. Set up your machine:

   1. Install [Anaconda][conda] (>=2.4.0) with Python 2.7 (!NOT! 3.x).
      We recommend you use [pyenv][] for this.

   2. Inside the project and with Anaconda activated, Install missing dependencies:

          pip install -r requirements.txt

3. Make sure the tests pass:

       nosetests

4. Create a feature branch:

       git checkout -b feature/my-awesome-changes

5. Make your change and gather them into contextual commits.
   Don't be too greedy with the number of commits you do.
   In general: don't put two unrelated changes into the same commit.

6. Add tests for your change. Make the tests pass:

       nosetests

7. Update and build the documentation:

       ./docs/update_apidocs.sh
       make html

8. Make sure you have committed everything.

9. Push to your fork and [submit a pull request][pr].

At this point you're waiting on us.
We may suggest some changes or improvements or alternatives.

Some things that will increase the chance that your pull request is accepted:

* Write tests.
* Write documentation for new modules, classes and methods.
* Comply to the style guide (see below).
* Write a [good commit message][commit].

[conda]: https://www.continuum.io/downloads
[pyenv]: https://github.com/yyuu/pyenv
[pr]: https://github.com/thoughtbot/factory_girl_rails/compare/
[commit]: http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html


# Style Guide

* Naming Conventions

  * all_lower_case with `_` (underscore) as whitespace replacements are:

    * folders
    * files
    * methods (member and non-member)

  * CamleCased are:

    * classes

  * ALL_CAPS with `_` (underscore) as whitespace replacements are:

    * constants (member and non-member)
