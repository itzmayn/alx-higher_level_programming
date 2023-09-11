#!/usr/bin/node
// imports 101 and excecutes thereafter. 

const callMeMoby = require('./101-call_me_moby').callMeMoby;
callMeMoby(3, function () {
  console.log('C is fun');
});
