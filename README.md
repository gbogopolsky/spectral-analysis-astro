# Spectral Analysis of Astronomical Data
Spectral analysis of astronomical data using Fourier and Morlet wavelet transforms.

## Running the notebook
If you want to run one of the notebooks of this repository, you just have to clone it on your computer using `git clone https://github.com/gbogopolsky/spectral-analysis-astro.git`.

Then, using Anaconda, create the virtual environment and run the Jupyter Notebook kernel:
```bash
conda create --name spectral-analysis --file requirements.txt
source activate spectral-analysis
jupyter notebook
```
And you're good to go. Enjoy!

## Building LaTeX source and .pdf file
Following these [instructions](https://nbconvert.readthedocs.io/en/latest/), make sure that the `pandoc` and `texlive-xetex` are installed on your distribution using `apt-get`, then create the LaTeX file using:
```bash
jupyter nbconvert --to latex --template article Rapport.ipynb
```

After some editing (presentation and removing one section level everywhere), run:
```bash
xelatex Rapport.tex
```

The output .pdf file is created.

## Thanks
I would like to thank Olga Alexandrova ([page](https://sites.lesia.obspm.fr/olga-alexandrova/)) and Baptiste Cecconi ([page](http://www.lesia.obspm.fr/perso/baptiste-cecconi/cursus.php)) from the LESIA lab of OBSPM for organising this practical session. Thanks also to C. Torrence, G. Compo and E. Predybaylo for developing the wavelet tranform routine in Python ([here](https://github.com/chris-torrence/wavelets) is the repository).
