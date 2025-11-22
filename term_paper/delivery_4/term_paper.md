---
title: "Term Paper"
subtitle: "OCP 5050 Fall 2025"
author: "Jorge Eduardo Velasco Zavala"
date: "2025-11-19"
geometry: 
    - margin=1in
    - letterpaper
bibliography: "references.bib"
csl: "modern-language-association.csl"

abstract: "In this study we studied the coupled upper-deep circulation variability in the Gulf of Mexico (GoM) using a high resolution 36 layer Hybrid Coordinates Ocean Model (HYCOM) simulation for the 1993-2019 period. By analyzing the thickness evolution of the isopycnal surfaces for a upper shallow layer (0-250m) and a deep layer (1000-2000m), interpreting the layer-thickness anomalies as hints of the changes in the internal pressure gradients to understand the mesoscale circulation patterns in the Gulf of Mexico. We applied a Complex Empirical Orthogonal Functions (CEOF) analysis to decompose the coupled upper-deep layer thickness variability. The first 4 modes explain about 61% of the total variance. Mode 1 alone accounts for 33.6% highlighting the dominant influence of Loop Current and Loop Current Eddy variability on upper-layer dynamics. While the upper patters obtained by our analysis are similar to the ones reported by Olvera-Prado et al. (2023), obtaining modal structures in terms of phase and amplitude, our lower layer decomposition show a more limited capability to identify coherent patters that can be associated to the deep Gulf of Mexico circulation. Future work will focus on the analysis of the Principal Components to understand the temporal evolution of these modes and associated characteristic time scales and extend the CEOF framework to incorporate SSH and additional dynamical fields to get a better understanding of the coupled upper-deep GoM interaction."
---

## Introduction

The Gulf of Mexico (GoM) is particularly interesting ocean dynamical region because it is a semi-enclosed basin dominated by a very energetic western boundary current known as the Loop Current. The Loop Current exhibits a large variability in penetration into the GoM, and it frequently sheds energetic anticyclonic eddies that propagated westward within the basin until they eventually dissipates.

TheGoM also holds substantial economic value for both the United States and Mexico due to its abundant natural resources, including oil, gas, fisheries, and tourism. Variability associated with the Loop Current and its eddies can significantly impact offshore operations, as the strong currents  may disrupt oil production and compromise the safety of offshore infrastructure and navigation.

The GoM exhibits a complex circulation system. However, it can be approximated as two-layer system in some modeling studies:an upper layer extending to approximately 800–1000 m that is largely modulated by surface-intensified flows, and a deep layer defined by depths greater than 1000–1200 m where currents tend to exhibit more homogeneous, nearly depth-independent behavior [@olvera-prado_upperlower_2023]; [@perez-brunius_dominant_2018].

In that sense, the surface GoM circulation is mainly dominated by the Loop Current System (LCS), which is the main circulation feature form the North Atlantic Western Boundary Current. [@brokaw_loop_2019], [@perez-brunius_dominant_2018]. This system can be further broken separated in the Loop Current (LC) and the Loop Current Eddies (LCE). The other main domination circulation pattern is the Campeche Gyre that is a semipermanent cyclonic circulation feature in the south of the GoM, in front of Campeche Bay[@olvera-prado_upperlower_2023], [@perez-brunius_dominant_2018], the positioning and intensity of this Gyre is linked to the LC cycle [@olvera-prado_upperlower_2023]

The Loop Current (LC), flow northward  entering into the GoM through the Yucatan Channel, bringing warm and saline Caribbean Sea Water and leaving through the Florida Straights where it fuses with the Gulf Stream [@brokaw_loop_2019], [@perez-brunius_dominant_2018].

The position of the LC has a varies widely, going from a retracted state where it is moves almost directly from Yucatan channel to Florida Straits to an extended state, where the LC reaches the  Mississippi-Alabama-Florida (MAFLA) Shelf [@brokaw_eddy_2020], [@brokaw_loop_2019], this behavior does not follow a strong seasonal cycle [@sturges_introduction_2005]. However, LC northward penetration and its tendency to shed eddies show a bimodal (biannual) seasonal signal, peaking in winter (Dec–Jan or Feb–Mar) and summer (Jun–Jul or Jul–Sep) influenced by the seasonal winds in the Caribbean Sea as consequence of the transport intensification [@chang_why_2012]. Also, smaller cyclonic eddies defined as Loop Current Frontal Eddies (LCFEs) congregate around the LC which sometimes strangulate the LC which might help the LCE shedding process.

When the LC is in extended state, it lead to the shedding of highly energetic anticyclonic Loop Current Eddies (LCEs), the eddies are quite large, typically around 200-300km in diameter [@sturges_introduction_2005, @perez-brunius_dominant_2018]. This separation events occur in irregular time scales from approximately 3 to 17 months as proposed by Sturges et al, 2000, as cited by [@olvera-prado_upperlower_2023, @chang_why_2012], once detached, these eddies drift westward across the GoM of Mexico, driving the deep circulation just about everywhere in the GoM [@sturges_introduction_2005].

In the deep gulf of Mexico there are three main circulation patterns: a cyclonic boundary current, a cyclonic gyre in the abyssal plain, and the very high eddy kinetic energy (EKE) region en the Eastern Gulf [@perez-brunius_dominant_2018], figures ref{fig:deep1} and ref{fig:deep2} taken from  [@perez-brunius_dominant_2018].

In figure ref{fig:deep1}, we have a baroclinic boundary current that flow around the Gulf of about 3 cm/s around most of the GoM and more evident in the wester region, along with a cyclonic gyre in the abyssal plain on the western basin with 5 cm/s speeds, which is know as the Sigsbee Abyssal Gyre (SAG) [@perez-brunius_dominant_2018].

![Deep Gulf of Mexico Circulation Patterns](images/perez_deep1.png){#fig:deep1 width=75%}

![Deep Gulf of Mexico Edddy Kinetic Energy](images/perez_deep2.png){#fig:deep2 width=75%}

In the deep Eastern GoM, we found the presence of very high EKE, figure \ref{fig:deep2} [@perez-brunius_dominant_2018], which is consequence of the LC expansion and retraction cycles.

## Data and Methods

### HYCOM Model

The Hybrid Coordinates Ocean Model (HYCOM) is a numerical model for ocean circulation, it is used to simulate the dynamics and variability of the ocean in 3 spatial dimension, the HYCOM main highlight over other numerical models is the use an hybrid approach to represent the vertical structure of the ocean column, which enable the model to represent each vertical layer as an isopycnal layers (constant density) in the open ocean, while switching to sigma coordinates that follow the ocean bathymetry in shallow or coastal regions and regular constant z coordinates above the mixing layer, figure \ref{fig:hycom-coords} taken from [@castaldi_pdf_nodate]. This allows the model to reproduce with good accuracy both the coastal and open ocean characteristics.

![HYCOM Vertical Hybrid Coordinates](images/hycom_vertical_coords.png){#fig:hycom-coords width=75%}

In order to analyze the circulation patterns in the shallow and deep Gulf of Mexico, a free-running ocean simulation forced only by wind coming from a WRF reanalysis. This configuration allows us to isolate the evolution of the ocean dynamics according to the primitive equations and the wind forcing, avoiding possible spurious variability induced by the data assimilation. So, the model output provides a physical consistent representation of the wind-driven component of ocean circulation, facilitates the detection of physically interpretable variability modes using techniques such as Complex Empirical Orthogonal Functions (CEOFs). The simulation setup employs 36 hybrid layers, a horizontal resolution of 1/25° resolution, and daily averaged outputs spanning 1993 to 2019.

### Isopycnal Surfaces

In this study, we are interested in comparing how the thickness of the isopycnal in the shallow and deep Gulf of Mexico varies over time. Changes in width of these surfaces directly reflect dynamical adjustments in the ocean horizontal circulation through their influence on pressure gradients. So, if over time an isopycnal thickens or thins, the associated tilting  modifies the pressure field and therefore change in the pressure gradients which directly drive the geostrophic flow, changing the current directions and strength. In analogy to how sea surface hight (SSH) gradients describe the surface geostrophic circulation, the gradient of the isopycnal thickness can be considered an internal SSH, capturing the geostrophic motions inside the ocean.

Because the LC and LCEs are approximately in geostrophic balance, the isopycnal layer thickness contours, as well as the SSH contours, closely follow the streamlines in the flow. Thus, it is assumed that the layer thickness variability is a good representation of the mesoscale field variability, [@olvera-prado_upperlower_2023].

To investigate the coupled upper–lower variability following the approach of [@olvera-prado_upperlower_2023], we separate the Gulf of Mexico circulation into two representative layers. The upper layer representative of the surface, extending from 0 m to approximately 250 m depth, by summing the individual thicknesses of layers 1-23 of our HYCOM simulation. The lower layer, representative of the Deep Gulf of Mexico, ranging approximately 1000 to 2000 m depth considering the thickness of the 30th and 31st layers from our free-running simulation. In figure \ref{fig:hycom-layers}, we show the average thickness of each of our model layers. For the deep layer we tested 2 configurations, one using the single 31th layer with a span of 1100 to 2000 m depth, and the other using the acummulated thickness of the 30th and 31st layers with a span of 1000 to 2000 m depth.

![HYCOM Layers Thickness and Depths](images/layer_mean_tk.png){#fig:hycom-layers width=75%}

For each grid point in both layers, we removed the trend and annual cycle from the time series along with variations on time scales shorter than 30 day in order to focus only on the mesoscale features. The data was then combined in an array in the $(time \times space)$ form to be used for the Complex EOF analysis.

### Complex Empirical Orthogonal Functions (CEOF) analysis

By computing the Hilbert transform across time we create an identical time series to our original data, with the exception of it being shifted by $\pi/2$ phase shift which is used to augment the information by adding the information of the future behavior of the time series vector $X_t$, [@storch_statistical_1999]. This is accomplished by combining the original vector time series $X_t$ and its Hilbert transform $X_t^H$ into a new complex vector time series [@storch_statistical_1999].

$$
H_t = X_t + iX_t^H
$$

By computing the Hilbert, it allows the data to be represented in a complex plane, where the phase describes the relative characteristic time and the amplitude describes the relative strength. When this complex field is decomposed using Principal Components (PC) and Empirical Orthogonal Functions (EOF), the resulting CEOF modes represent space–time oscillations, including propagating signals. These patterns are very valuable for identifying recurrence in the circulation in the Gulf of Mexico and couplings between the upper and deep layers.

In climate studies (including oceanic and atmospheric sciences), the Empirical Orthogonal Function (EOF) analysis is widely used to identify spatial patterns of variability and their evolution. However, it does not follow physical principles: instead, it decomposes data into mathematically orthogonal (linearly independent basis) modes which may be linked to atmospheric and oceanographic phenomenon. Typically, the EOFs are derived by computing the eigenvalues and eigenvectors of an anomaly covariance matrix [\@ref{national_center_for_atmospheric_research_staff_eds_nodate}] However, a more efficient way to do so is, using the SVD decomposition which allow implicitly compute the covariance matrix, in the form:

$$
H = U S V^*
$$

which produces:

- $\mathbf{U}$ contains the complex temporal principal components (PCs),
- $\mathbf{S}$ Singular Values
- $\mathbf{V}$ contains the complex spatial patterns (CEOFs)
and the product of $US$ gives you the principal components PC scaled by the variance of each mode.

The singular values are directly linked to the amount of variance explained by each individual mode by

$$
\lambda_i = \frac{S_i^2}{N_t - 1}
$$

where $\lambda_i$ is the covariance explained by mode $i$ and $N_t$ the time steps analyzed, and if we normalize by $\Sigma \lambda_i$, we obtain the percentage of variance explained for each mode. So doing some linear algebra we can create dimensionless PCs with unit variance and EOF patterns scaled by the variance carried by their corresponding mode.

## Results

![Explained Variance](ticklayer/frac_var.png){#fig:frac-var width=75%}

In figure \ref{fig:frac-var} we show the explained variance for each mode, the firt mode explain 33.6%, the second mode explain 12.5%, the third mode explain 7.9%, and the fourth mode explain 7.1%. So, the total recovered variance for these first four leading modes is 61.1%.

The first 4 modes of the CEOF analysis for the experimentr using the deep layer from 1000 to 2000m depth, are shown in figures \ref{fig:ceof-mode1} to \ref{fig:ceof-mode4} and using these firt four modes we created phase and amplitude maps of the upper and deep layers, in figures \ref{fig:ceof-phase-amp-mode1} to \ref{fig:ceof-phase-amp-mode4} where the amplitude is represented by the color gradients and the phase is represented by the arrows. As mentioned by [@olvera-prado_upperlower_2023], the phase vector have arbitrary origin, so the direction they are pointing is not linked to a geographic location but how the direction of the vector change from one particular location with respect to another. The first mode, phase map ref{fig:ceof-phase-amp-mode1} represent a very large amplitude about $\pm$ 100 meters approximately and it is mostly located in north and east GoM wand if looking at the CEOF mode ref{fig:ceof-mode1} we observe we have a periodid  pater going from a weak negative anomali in the easternmost part followed by a strong positive anomaly and changing sigh again to a strong negative anomalyan finally a slightly weaker positive anomaly in the westernmost part of part of high amplitude anomalies, where the Loop Current System exhihits a very strong influence in the Gulf dynamics. In lower Gulf of Mexico we observe a much weaker amplitude responce figure ref{fig:ceof-phase-amp-mode1}, in this case the max amplitude is about $\pm$ 20 - 30 meters andan is mostly located close to  the Campehe Slope and Mississippi Canyon, and the phases are also very small only showing responses in these 2 locations.

The second mode, figure ref{fig:ceof-mode2} and ref{fig:ceof-phase-amp-mode2} represent a smaller amplitude pattern about 60 meters in amplitude whit a cyclonic patter detectable in the phase map located in the easth of the GoM, but the max amplitud is showin in the western region around the Sigsbee scarpment and Sigsbee plain and in the Lower layer we can observe a weaker response around the Sigsbee scarpment but it is just about $\pm$ 10 meters, and a secundary also weak response also close to Campeche Slope.

In the modes 3 and 4, figures ref{fig:ceof-mode3} and ref{fig:ceof-mode4} we still observe the stonger response in the easther regions of the upper layer, in this case the amplitudes in the upper layer are very close the the ones of the firts mode, about $\pm$ 60 and $\pm$ 45$ meter respectibly. Interestingly,m in the deep layer eve if the responses are much eaker consistently we observe that the highes amplitudes are usually in the northern boundary of Gulf of Mexico.

![CEOF Mode 1](ticklayer/EOF_mode_1_rescaled.png){#fig:ceof-mode1 width=75%}

![CEOF Mode 2](ticklayer/EOF_mode_2_rescaled.png){#fig:ceof-mode2 width=75%}

![CEOF Mode 3](ticklayer/EOF_mode_3_rescaled.png){#fig:ceof-mode3 width=75%}

![CEOF Mode 4](ticklayer/EOF_mode_4_rescaled.png){#fig:ceof-mode4 width=75%}

![Mode 1 Phase and Amplitude Maps](ticklayer/phase_amp_mode_1.png){#fig:ceof-phase-amp-mode1 width=75%}

![Mode 2 Phase and Amplitude Maps](ticklayer/phase_amp_mode_2.png){#fig:ceof-phase-amp-mode2 width=75%}

![Mode 3 Phase and Amplitude Maps](ticklayer/phase_amp_mode_3.png){#fig:ceof-phase-amp-mode3 width=75%}

![Mode 4 Phase and Amplitude Maps](ticklayer/phase_amp_mode_4.png){#fig:ceof-phase-amp-mode4 width=75%}

Finally we also created a Map of the proporcional explained variance for the first 4 leading modes, in figure ref{fig:frac-var-map}. In this map we can observe that the firts four modes explain upto about 80% of the variance of the upper variability in most of the Golf of Mexico, however, it has problems to capture the variability in the region offshore of Veracruz and South of Tampico Regions, and struggles even more to capture the variability of the deep layer, with only about 40% of the variance and only in very limited regions, mostly around the slope of the continental shelf.

![Maps of the proportional explained variance for the first 4 leading modes for the upper and deep layers](ticklayer/EV_maps.png){#fig:frac-var-map width=75%}

## Discussion

In the original paper by [@olvera-prado_upperlower_2023], the author found that the firts 4 modes explains about 50% of total variance, with fractions of 23%, 12%, 8%, and 6% respectively, in figure ref{fig:amplitudes-phases-olvera} we can observe the amplitudes and phases of the first 4 modes found by [@olvera-prado_upperlower_2023], and in figure ref{fig:frac-var-map-olvera} we can observe the maps of the explained variance for the first 4 modes found by [@olvera-prado_upperlower_2023]. Comparing our results with the original paper, we can observe that the the modes we recovered captures about 10% more variance than the original paper, with fractions and in particular the first mode explain 33.6% of the variance compared to 23% in the original paper, if we look at the amplitude and phase maps form this first mode even if the phases follow the same patter in the upper mlayer but with the opposite sign, and the lower layer amplitude map also is similar but nthe mode we found fails to capture the variability the same amplitude that the original paper does in the lower layer, hoever there are some concidence in the the campeche slope and Mississippi Canyon regions, but they do not extent as much as in the original paper.

Mode 2 in the original paper explains 12% of the variance, that is very similar to the 12.5% of the variance we found in our analysis, and we can observe that again we have concidences in the phase and amplitude maps in the upper layer. However, our decomposition of the modes strugles to capture the varibaility of the deep layer. Which is consistent whit what we observe in the maps of the explained variance \ref{fig:frac-var-map} and \ref{fig:frac-var-map-olvera}, where we can observe thatn the amounts and location of the variance explained are very similar in the upper layer but the deep layer in our analysis is much more limited compared to [Olvera-Prado et al. (2023)].

![Amplitudes and Phases of the first 4 leading modes found by Olvera-Prado et al. (2023)](images/olvera_couppledmodes.png){#fig:amplitudes-phases-olvera width=75%}

![Maps of explained variance for the first 4 leading modes found by Olvera-Prado et al. (2023)](images/explained_vartiance.png){#fig:frac-var-map-olvera width=75%}

## Conclusion and Future Work

In this study we have analyzed the circulation in the Gulf of Mexico using the HYCOM model and the Complex Empirical Orthogonal Functions (CEOF) analysis. We have found that the firts 4 modes explain about 61.1% of the variance of the coupled upper-lower layer variability in the Gulf of Mexico, which is consistent with the results found by [@olvera-prado_upperlower_2023]. However, we have found that our analisys of deep circulation is very sensible to the depth isopicnal layer used as representative of the deep circulation, given that our analysis uses a deep layer from 1000 to 2000m depth which we expected to be a good approximation of the one used by [@olvera-prado_upperlower_2023], but we found that the capability to detect deep ocean circulation is more limited compared to the original paper.

Even if we strugle to capture the amplitude an phase of the deep circulation as well defined as in the original paper taken as inspiration, we still need to get a better understanding of the deep circulation in the Gulf of Mexico and also analyse the Principal Components (PC) as future work in orther to stablish the time scale dominances of the four leading modes I found. Also, extending the analysis to also include the SSH or other variables to the CEOF analysis  to get a better picture of the correlations between the different variables in the dynamics of the Gulf of Mexico.

## References
