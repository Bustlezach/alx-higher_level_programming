#!/usr/bin/node

import { list } from './100-data.js';

const new_arr = list.map((cur, i) => cur * i);
console.log(list);
console.log(new_arr);
