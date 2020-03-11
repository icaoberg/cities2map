#!/bin/bash

conda create --name cities2map
conde activate cities2map
conda install basemap
conda install basemap-data-hires
conda install -c conda-forge geopy
conda install pandas
conda install click
conda install matplotlib
conda deactivate
