#!/bin/bash

if [ "$#" -ne 1 ]; then
	echo "Illegal number of parameters. Usage: ./setup.sh ProjectName"
	exit 1
fi

mkdir "$1"

echo "Do you need an External Penetration Test folder? yes/no"
read EPTanswer

echo "Do you need an Internal Penetration Test folder? yes/no"
read IPTanswer

if [[ "$EPTanswer" == "yes" ]]; then
	mkdir -p "$1/EPT/evidence/credentials"
	mkdir -p "$1/EPT/evidence/data"
	mkdir -p "$1/EPT/evidence/screenshots"
	mkdir -p "$1/EPT/logs"
	mkdir -p "$1/EPT/scans"
	mkdir -p "$1/EPT/scope"
	mkdir -p "$1/EPT/tools"
fi

if [[ "$IPTanswer" == "yes" ]]; then
	mkdir -p "$1/IPT/evidence/credentials"
	mkdir -p "$1/IPT/evidence/data"
	mkdir -p "$1/IPT/evidence/screenshots"
	mkdir -p "$1/IPT/logs"
	mkdir -p "$1/IPT/scans"
	mkdir -p "$1/IPT/scope"
	mkdir -p "$1/IPT/tools"
fi

