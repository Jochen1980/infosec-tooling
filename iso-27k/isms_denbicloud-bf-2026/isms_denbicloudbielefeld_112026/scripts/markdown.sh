#!/usr/bin/env bash
if [[ ${HOME} == "/homes/"* ]]; then
  export RUBYOPT=-EUTF-8
  gem install --user-install mdl &> /dev/null || echo "gem install failed"
  ${HOME}/.gem/ruby/2.5.0/bin/mdl --style .mdl-style.rb ./ && echo "OK"
else
  docker run --rm -v ${PWD}:/workdir/ --env RUBYOPT=-EUTF-8 -i bidenbi/markdown-lint mdl --style /workdir/.mdl-style.rb /workdir && echo "OK"
fi
