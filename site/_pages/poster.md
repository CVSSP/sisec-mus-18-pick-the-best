---
layout: poster
title:  "My Poster"
permalink: /poster/
---

<div id='title'>

<h1>SiSEC 2018</h1>
<h1>
<span style='color: #1b656d'>
STATE OF THE ART IN MUSICAL AUDIO SOURCE SEPARATION
</span>
</h1>

<h1>
<span style='color: #1b656d'>
SUBJECTIVE SELECTION OF THE BEST ALGORITHM
</span>
</h1>

<div style='width: 50%; float: left' markdown="1">
<h2>Dominic Ward, Russell D. Mason, </h2>
<h2>Chungeun Kim, Mark D. Plumbley</h2>
<h3>CVSSP | IoSR | University of Surrey, Guildford, UK </h3>
</div>

<div style='width: 50%; float: right' markdown="1">
<h2>Fabian-Robert Stöter, Antoine Liutkus</h2>
<h3>Inria and LIRMM | University of Montpellier, France</h3>
</div>

</div>

<div id='title-info'>

<div>
<img style='width: 100%; margin: 0; padding: 25px; float: left' src="{{ site.url }}/images/uos.png">
<img style='width: 100%; margin: 0; padding: 25px; float: left' src="{{ site.url }}/images/epsrc.png">
</div>

</div>

<div class='panel' id='intro' markdown="1">

# SiSEC 2018 : MUS(ic) Task

- The Signal Separation Evaluation Campaign (SiSEC) is a
  large-scale regular event aimed at evaluating current progress in source
  separation <sup>1</sup> 

-  The MUS(ic) separation task compares algorithms aimed at
  recovering instrument stems from a stereo mix

- This work focuses on _singing-voice separation_

- Deep-learning methods show significant improvements over traditional
  techniques such as NMF and ICA

- Source separation introduces distortions and artifacts, which degrade the
  perceived sound quality

<div class='refs' markdown="1">
- Stöter et al. (2018) { [10.1007/978-3-319-93764-9_28](https://doi.org/10.1007/978-3-319-93764-9_28) }
</div>

</div>

<div class='panel' id='intro2' markdown="1">

# How To Evaluate Separation Performance?

Few researchers conduct listening assessments, but instead rely on objective
toolkits to quantify separation performance:

- <span style='color: #1b656d'>BSS Eval</span> <sup>2</sup>: Blind Source Separation Evaluation
- <span style='color: #1b656d'>PEASS</span> <sup>3</sup>: Perceptual Evaluation methods for Audio Source Separation

Both approaches based on distortion decomposition between estimated source
$$\hat{S}$$ and target source $$S$$:

$$\hat{S} - S = e_{\text{target}} + e_{\text{interference}} + e_{\text{artifacts}}$$

Error components estimated through least-squares projections of estimated and
true sources:

![]({{ site.url }}/images/bss_eval.png)

<div class='refs' markdown="1">
- Vincent et al. (2006) { [10.1109/tsa.2005.858005](https://doi.org/10.1109/TSA.2005.858005) }
- Emiya et al. (2012) { [10.1109/tasl.2011.2109381](https://doi.org/10.1109/tasl.2011.2109381) }
</div>

</div>

<div class='panel-emph' id='method1' markdown="1">
# Subjective Listening Assessment

- 13 songs, with singing-voice as the target source

- 34 listeners compared 6 deep-learning algorithms, selected from 30 SiSEC
    systems: <sup>4</sup>

  - <span style='color: #1b656d'>**TAK2**</span>: Multi-scale multi-band DenseLSTM
  - <span style='color: #1b656d'>**TAU1**</span>: Blending of MMDenseNets and LSTM (UHL3)
  - <span style='color: #1b656d'>**UHL3**</span>: Bi-directional LSTM with 3 BLSTM layers 
  - <span style='color: #1b656d'>**JY3**</span>: Denoising auto-encoder with skip connections
  - <span style='color: #1b656d'>**STL1**</span>: Wave-U-Net for end-to-end audio source separation
  - <span style='color: #1b656d'>**MDL1**</span>: Recurrent inference algorithm with masker and denoiser architecture

<div class='refs' markdown="1">
- Algorithm info / GitHub repos { [https://bit.ly/2CukSMd](https://bit.ly/2CukSMd) }
</div>

</div>

<div class='panel-emph' id='method2' markdown="1">
# Subjective Listening Assessment

> Your task is to pick 1 out of 6 test sounds that is most similar to a 
> recording of singing-voices.
> The best source separation method should produce a test sound that is
> perceptually identical to the original recording.

![]({{ site.url }}/images/interface.png)
*Listening test GitHub repo { [https://bit.ly/2NXeVsK](https://bit.ly/2NXeVsK) }*

</div>

<div class='panel' id='results' markdown="1">

# Results

<div markdown="1">
![]({{ site.url }}/images/algo_boxplots.png)
*Strip and box plots showing the number of times each algorithm was selected for a given
song, normalised by the total number of listeners*
</div>

<div markdown="1">
![]({{ site.url }}/images/correlations.png)
*Spearman correlation between the observed frequency
counts of the test stimuli, and the corresponding OPS/SDR values,
separated by song*
</div>


</div>

<div class='panel' id='conclusions' markdown="1">

# Conclusions

- <span style='color: #1b656d'>**TAU1**</span> performed best, followed by <span style='color: #1b656d'>**TAK2**</span>
- Listeners' selection of the best algorithm depended on song (see <span style='color: #1b656d'>**JY3**</span> above)
- SDR of the BSS Eval toolkit gave the highest correlations (higher SDR = more votes)
- More controlled assessments, involving trained listeners, using scaling procedures to quantify overall separation quality are needed
- Further work needed to assess/refine objective metrics of overall separation quality

</div>
