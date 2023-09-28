#!/bin/bash

url=$1
user_id_header="X-School-User-Id: 98"
curl -X GET -H "$user_id_header" "$url"
