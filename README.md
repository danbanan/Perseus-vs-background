# Astrophysics Machine Learning Project

## Classifying Foreground Dwarfs and Background Giants in the Perseus Cluster

Looking at previous tests with photo-z we were able to tell the difference 
between Perseus cluster galaxies from background galaxies with true redshift 
~>0.08. However, we have a hard time differentiating foreground galaxies from background galaxies with redshift between ~0.04 and 0.07. In a previous research assignment, Dan compared visually foreground dwarf galaxies to background giant galaxies in the Perseus cluster with redshifts that falls within this particular range. He found that there were a lot of similarities, especially in shape, but 
you could tell the difference by comparing the size and intensity of color 
between the two galaxy groups.

**Project Goal:** Help out with completing the Perseus cluster catalog by using machine learning to see if there are any other paramaters besides true redshift 
that can discriminate between foreground dwarf galaxies in the Perseus cluster 
and giant background galaxies.

```
├── PerseusDwarfs               <--- Previous assignment of similar topic
│   ├── PerseusDwarfs.ipynb
│   ├── background_galaxies.csv
│   ├── background_galaxies.png
│   ├── dwarf_galaxies.csv
│   ├── dwarf_galaxies.png
│   ├── dwarf_galaxies2.png
│   ├── only_background.csv
│   ├── only_background.png
│   ├── only_dwarfs.csv
│   ├── only_dwarfs.png
│   ├── plausible_galaxies.csv
│   ├── plausible_galaxies.png
│   └── search_area.png
├── README.md
├── background-filter.ipynb     <--- Filter everything but background giants
├── complete                    <--- Merged datasets of SDSS and NED redshifts
│   ├── background.csv          <--- Training data for background giants
│   ├── dwarfs.csv              <--- Training data for foreground dwarfs
│   ├── ngc383.csv
│   └── ngc507.csv
├── cross-id                    <--- Datasets from NED formatted for CrossID search
│   ├── ngc383.csv
│   └── ngc507.csv
├── datasets-txt                <--- Datasets from NED search in txt format
│   ├── Perseus_NED.txt
│   └── back_NED.txt
├── dwarfs-filter.ipynb         <--- Filter everything out but foreground dwarfs
├── helper.py                   <--- Converts txt format to csv format
├── ned                         <--- Datasets from NED search in csv format
│   ├── ngc383.csv
│   └── ngc507.csv
├── ngc383-redshifts.ipynb      <--- Data analysis of NGC 383 redshifts
├── ngc507-redshifts.ipynb      <--- Data analysis of NGC 507 redshifts
├── perseus.ipynb               <--- Creating test data for Perseus cluster
└── sdss                        <--- SDSS datasets of the stellar objects found in
    ├── ngc383.csv
    └── ngc507.csv
```

As previously mentioned we have a hard time differentiating foreground dwarfes 
from background galaxies by only looking at the the photometric redshifts. To 
label galaxies as foreground dwarfs or background galaxies we need to look at
true redshift, and the spectroscopic redshift is the closest one to that. SDSS library misses a lot of spectroscopic redshifts of different stellar objects. 
Fortunately we can retrieve many of the missing spectroscopic redshifts from 
NED. In NED we are limited to a search radius of 60 arcminutes. We combine the
dataset from the NED search with the SDSS library using CrossID. In CrossID we
set the search radius of each object to be 0.03 arcminutes to make sure that we
CrossID the right objects from SDSS and NED. We then merge the spectroscopic
redshifts from NED with the resulting dataset from CrossID. Now we have datasets
ready for data analysis.

The data analysis on the redshifts of NGC 383 dataset shows us that galaxies 
with redshifts between 0.0125 and 0.0225 are in the foreground of the cluster.
We performed the same data analysis on the NGC 507 dataset and found the 
redshift range of foreground galaxies to be from 0.012-0.022.

*Please look at note book ngc383-redshifts and ngc507-redshifts for further more
details.*

Our next step was to use these redshift ranges to create datasets of foreground
dwarf galaxies and background giants.

**From NGC 383 and 507 we have in total 26 dwarfs and 31 background galaxies.**

This is very little data. The question is: Is there a way to to search the whole 
sky for dwarf galaxies and background galaxies within SDSS? The dwarf galaxies 
in Perseus are all ellipticals so we need dwarfs of similar color, size and redshift. Increasing the set of background galaxies might be more challenging 
and we do not currently have an idea to do so.

If we are unable to increase our data sets, we will move forward and try to 
perform more data analysis on the datasets we have, and start building a model.