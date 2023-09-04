#!/bin/bash
# Autor: Christofer Borrayo
# @christoferborrayo8
docker build -t i_odoo_filter:16 -f Dockerfile_odoo .
docker build -t i_postgres_filter:13 -f Dockerfile_postgres . 
docker-compose up