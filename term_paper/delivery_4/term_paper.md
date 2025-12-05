---
title: "Term Paper: Variability of Upper and Lower Layer Gulf of Mexico Circulation from Isopycnal Thickness Anomalies"
subtitle: "OCP 5050 Fall 2025"
author: "Jorge Eduardo Velasco Zavala"
date: "2025-11-19"
geometry: 
    - margin=1in
    - letterpaper
bibliography: "references.bib"
csl: "modern-language-association.csl"

abstract: "In this study we studied the coupled upper-deep circulation variability in the Gulf of Mexico (GoM) using a high resolution 36 layer Hybrid Coordinates Ocean Model (HYCOM) simulation for the 1993-2019 period. By analyzing the thickness evolution of the isopycnal surfaces for a upper shallow layer (0-250m) and a deep layer (1000-2000m), interpreting the layer-thickness anomalies as hints of the changes in the internal pressure gradients to understand the mesoscale circulation patterns in the Gulf of Mexico. We applied a Complex Empirical Orthogonal Functions (CEOF) analysis to decompose the coupled upper-deep layer thickness variability. The first 4 modes explain about 50% of the total variance. Mode 1 alone accounts for 22.8% highlighting the dominant influence of Loop Current and Loop Current Eddy variability on upper-layer dynamics. The other modes explain about 18%, 10% and 6% of the total variance respectively.
The explained variance maps recovered by using only the first 4 leading modes show that the our modes capture a very good amount of the variability in the upper layer, specially in the nothern region of the GoM, while at the same time we also capture a decent amount of the variability in the deep layer. However, this high explainability in the deep Gulf of Mexico seems to be bounded to slope bounded circulation patterns and therfore it might be highly correlayed to the boundary current that sorrounds the Abyssal Plain in the Gulf of Mexico. Future work will focus on the analysis of the Principal Components to understand the temporal evolution of these modes and associated characteristic time scales and extend the CEOF framework to incorporate SSH and additional dynamical fields to get a better understanding of the coupled responses in the Gulf of Mexico."
---

## Introduction

The Gulf of Mexico (GoM) is particularly interesting ocean dynamical region because, it is a semi-enclosed basin dominated by a very energetic western boundary current known as the Loop Current. The Loop Current exhibits a large variability in penetration into the GoM, and it frequently sheds energetic anticyclonic eddies that propagates westward within the basin until they eventually dissipates. The GoM also holds substantial economic value for both the United States and Mexico due to its abundant natural resources, including oil, gas, fisheries, and tourism. Variability associated with the Loop Current and its eddies can significantly impact offshore operations, as the strong currents may disrupt oil production and compromise the safety of offshore infrastructure and navigation.

The GoM exhibits a complex circulation system. However, it can be approximated as two-layer system in some modeling studies: an upper layer extending to approximately 800–1000 m that is largely modulated by surface-intensified flows, and a deep layer defined by depths greater than 1000–1200 m where currents tend to exhibit more homogeneous, nearly depth-independent behavior [@olvera-prado_upperlower_2023], [@perez-brunius_dominant_2018].

In that sense, the surface GoM circulation is mainly dominated by the Loop Current System (LCS), which is the main circulation feature form the North Atlantic Western Boundary Current. [@brokaw_loop_2019], [@perez-brunius_dominant_2018]. This system can be further broken separated in the Loop Current (LC) and the Loop Current Eddies (LCE). The other main domination circulation pattern is the Campeche Gyre that is a semipermanent cyclonic circulation feature in the south of the GoM, in front of Campeche Bay[@olvera-prado_upperlower_2023], [@perez-brunius_dominant_2018], the positioning and intensity of this Gyre is linked to the LC cycle [@olvera-prado_upperlower_2023]

The Loop Current (LC), flow northward entering into the GoM through the Yucatan Channel, bringing warm and saline Caribbean Sea Water and leaving through the Florida Straights where it fuses with the Gulf Stream [@brokaw_loop_2019], [@perez-brunius_dominant_2018].

The position of the LC has a varies widely, going from a retracted state where it moves almost directly from Yucatan channel to Florida Straits to an extended state, where the LC reaches the  Mississippi-Alabama-Florida (MAFLA) Shelf [@brokaw_eddy_2020], [@brokaw_loop_2019], this behavior does not follow a strong seasonal cycle [@sturges_introduction_2005]. However, the LC northward penetration and its tendency to shed eddies show a bimodal (biannual) seasonal signal, peaking in winter (Dec–Jan or Feb–Mar) and summer (Jun–Jul or Jul–Sep) influenced by the seasonal winds in the Caribbean Sea as consequence of the transport intensification [@chang_why_2012]. Also, smaller cyclonic eddies defined as Loop Current Frontal Eddies (LCFEs) congregate around the LC which sometimes strangulate the LC which might help the LCE shedding process.

When the LC is in extended state, it lead to the shedding of highly energetic anticyclonic Loop Current Eddies (LCEs), the eddies are quite large, typically around 200-300km in diameter [@sturges_introduction_2005], [@perez-brunius_dominant_2018]. This separation events occur in irregular time scales from approximately 3 to 17 months as proposed by Sturges et al, 2000, as cited by [@olvera-prado_upperlower_2023], [@chang_why_2012], once detached, these eddies drift westward across the GoM of Mexico, driving the deep circulation just about everywhere in the GoM [@sturges_introduction_2005].

In the deep gulf of Mexico, there are three main circulation patterns: a cyclonic boundary current, a cyclonic gyre in the abyssal plain, and the very high eddy kinetic energy (EKE) region en the Eastern Gulf [@perez-brunius_dominant_2018], figures \ref{fig:deep1} and \ref{fig:deep2} taken from  [@perez-brunius_dominant_2018].

In figure \ref{fig:deep1}, we have a baroclinic boundary current that flow around the Gulf of about 3 cm/s around most of the GoM and more evident in the wester region, along with a cyclonic gyre in the abyssal plain on the western basin with 5 cm/s speeds, which is know as the Sigsbee Abyssal Gyre (SAG) [@perez-brunius_dominant_2018].

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

To investigate the coupled upper–lower variability following the approach of [@olvera-prado_upperlower_2023], we separate the Gulf of Mexico circulation into two representative layers. The upper layer representative of the surface, extending from 0 m to approximately 250 m depth, by summing the individual thicknesses of layers 1-23 of our HYCOM simulation. The lower layer, representative of the Deep Gulf of Mexico, ranging approximately 1000 to 2000 m depth considering the thickness of the 31st and 32nd layers from our free-running simulation. In figure \ref{fig:hycom-layers}, we show the average thickness of each of our model layers. For the deep layer we used the average thickness of the 31st and 32nd layers.

![HYCOM Layers Thickness and Depths](images/layer_mean_tk.png){#fig:hycom-layers width=75%}

For each grid point in both layers, we removed the trend and annual cycle from the time series along with variations on time scales shorter than 30 day and a Lanczos low-pass filter of 100 kilometers in order to focus only on the mesoscale features. The data was then combined in an array in the $(time \times space)$ form to be used for the Complex EOF analysis.

### Complex Empirical Orthogonal Functions (CEOF) analysis

By computing the Hilbert transform across time we create an identical time series to our original data, with the exception of it being shifted by $\pi/2$ phase shift which is used to augment the information by adding the information of the future behavior of the time series vector $X_t$, [@storch_statistical_1999]. This is accomplished by combining the original vector time series $X_t$ and its Hilbert transform $X_t^H$ into a new complex vector time series [@storch_statistical_1999].

$$
H_t = X_t + iX_t^H
$$

By computing the Hilbert, it allows the data to be represented in a complex plane, where the phase describes the relative characteristic time and the amplitude describes the relative strength. When this complex field is decomposed using Principal Components (PC) and Empirical Orthogonal Functions (EOF), the resulting CEOF modes represent space–time oscillations, including propagating signals. These patterns are very valuable for identifying recurrence in the circulation in the Gulf of Mexico and couplings between the upper and deep layers.

In climate studies (including oceanic and atmospheric sciences), the Empirical Orthogonal Function (EOF) analysis is widely used to identify spatial patterns of variability and their evolution. However, it does not follow physical principles: instead, it decomposes data into mathematically orthogonal (linearly independent basis) modes which may be linked to atmospheric and oceanographic phenomenon. Typically, the EOFs are derived by computing the eigenvalues and eigenvectors of an anomaly covariance matrix [@national_center_for_atmospheric_research_staff_eds_nodate] However, a more efficient way to do so is, using the SVD decomposition which allow implicitly compute the covariance matrix, in the form:

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

where $\lambda_i$ is the covariance explained by mode $i$ and $N_t$ the time steps analyzed, and if we normalize by $\Sigma \lambda_i$, we obtain the percentage of variance explained for each mode. By doing some aditional linear algebra, we can create dimensionless PCs with unit variance and EOF patterns scaled by the variance carried by their corresponding mode.

## Results

![Explained Variance](final_results/frac_var.png){#fig:frac-var width=75%}

In figure \ref{fig:frac-var}, we show the explained variance for each mode, the firt mode explain 22.8%, the second mode explain 18.2%, the third mode explain 10.5%, and the fourth mode explain 6.8%. So, the total recovered variance for these first four leading modes is 58.3%.

The first 4 modes of the CEOF analysis are shown in figure \ref{fig:ceof-modes} and using these modes, we created phase and amplitude maps of the upper and deep layers, in figure \ref{fig:ceof-phase-amp} where the amplitude is represented by the color gradients and the phase is represented by the arrows, as mentioned by [@olvera-prado_upperlower_2023], the phase vector have arbitrary origin, so the direction they are pointing is not linked to a geographic location but how the direction of the vector changes from one particular location with respect to another.

The first mode phase and amplitude map, figures \ref{fig:ceof-phase-amp}a and \ref{fig:ceof-modes}b, represet a very similar maximum amplitude in both the upper and lower layer, around 85 meters approximately with the lower layer having a slightly higher amplitude. In the upper layer, figure \ref{fig:ceof-phase-amp}a, we observa a almost full GoM high amplitude region, with the 3 coherent patterns, two of them seem to diverge and in the middle of this to divergence region, we identify a the third pattern, that as opposed to the other two patterns it shows a convergneces, around the 88W longitude in the northern part of the GoM, looking at the CEOF map, \ref{fig:ceof-modes}a, we observe that the divergence regions are associated to negative anomalies and the convergence region is associated to positive anomalies, however, the is no appreciable full phase change pattern in the phase map, so it might be a stationary baroclinic mode, associated to the Loop Current and Loop Current Eddies evolution.

In the lower layer, figure \ref{fig:ceof-phase-amp}b, we can observe a different structure, the maximum amplitude is reached in a much more localized region, around the 88W longitude in the North GoM, close to the convergence region of the upper layer, which suggest an ajustment in the deep circulations associated to the effect of the upper mode, if we look at the CEOF map, \ref{fig:ceof-modes}b, we observe that the anomaly is negative in this region, opposite to the upper layer anomaly, so this is a good indication of a coupling between the upper and deep layers response to the Loop Current and Loop Current Eddies evolution. In the west and northwest part of the GoM we can observe some coherent signal with the same phase along with the Sigsbee plain boundary, suggesting a slope trapped response that seems to be stationary.

The second mode phase and amplitude map, figures \ref{fig:ceof-phase-amp}c and \ref{fig:ceof-modes}d, we notice that the amplitude in the upper layer is mush weaker than the complementary amplitude in the lower layer, almost half the amplitude. The upper mode closely resembles the first upper mode with a similar but more constrained region of action but the phases are similar to the ones of the firts mode. The largest amplitude region is equivalent to the one found in the first mode, figure \ref{fig:ceof-modes}a, and also we can clearly see a new convergence region near ~93W that is also present on the first mode but, much weaker, in this second mode is clearly visible. Looking at the CEOF map, \ref{fig:ceof-modes}c, we can observe that the the patten is also similar to the first mode, buth the signs are inverted, so this might be a counterbalance to the first mode in the upper layer, that is also associated to the dominance of the Loop Current System.

The lower layer mode, figure \ref{fig:ceof-phase-amp}d, it also similar to the first mode, however, it stands out that the amplitude in this mode is much stronger and we observe a coherent responsers that follow the the boundary of the Sigsbee plain in the North, West and Southwestern part of the GoM, also stands out that the previously detached high amplitude region around the 88W longitude is fully integrated with the previously detached region in west, so this suggest a slope trapped response. Looking at the CEOF map, \ref{fig:ceof-modes}d, we can observe that there is a clear delimitation between the abyssal plain and the boundary slope region.

The third mode phase and amplitude map, figures \ref{fig:ceof-phase-amp}e, we can observe that this time the high amplitude region is located in the North west part of the GoM, close to where the identify a new convergence region in the previous mode, and also an anticlockwise rotation pattern in the eastern region. This pattern is not necessarily indicator of a cyclonic circulation pattern, but a region of high variability. It is interesting that the CEOF map, \ref{fig:ceof-modes}f, shows to dipoles centered around this two high amplitude regions. In the deep layer we observe that there is only a single and very localized high amplitude region, just above to the convergence zone identified in the previous mode, which indicates a coupled response associated to the upper layer mode. Looking at the CEOF map, \ref{fig:ceof-modes}f, we observe that the sign of this anomaly is opposite to the upper layer anomaly, so this might be a negative counterbalance to the upper layer mode.

Looking at the fourth upper layer mode phase, figure \ref{fig:ceof-phase-amp}g, we observe a more regional structure where in the north part we observe a westward propagation pattern, that curves down and change propagation direction in the east, and in the lower layer we observe a many region with high amplitudes with phases that at some regions seems to align with the topographic features of the GoM, so this mode might still be deeply associated to the topographic bounded circulation patterns that are present in the GoM. However, we can observe that again the max amplitude region in the upper layer is in the northern region and it is coincident with one of the high amplitude regions in the lower layer, so this suggest another coupled adjustment due to the interaction of the upper and lower layers. Looking at the CEOF map, \ref{fig:ceof-modes}g and \ref{fig:ceof-modes}h, we observe that the sign of the anomaly in the coupling regions seems to be the same so this mean that both layers are responding in a very similar way.

![Firts 4 CEOF leading modes](final_results/Amplitude_EOFs_nvars2.png){#fig:ceof-modes width=80%}

![Amplitude and Phase Maps of the first 4 CEOF leading modes](final_results/Mosaic_EOFs_nvars2.png){#fig:ceof-phase-amp width=80%}

Finally, we also created a Map of the proporcional explained variance for the first 4 leading modes, in figure \ref{fig:frac-var-map}. In this map we can observe that the firts four modes explain  upto 80% or even more of the variance of the upper variability in most of the Golf of Mexico. Which indicates that the upper layer variability is very well captured by the CEOF analysis. Also looking at the deep layer explained variance map we observe that the reconstruction is more limited, with only about 50% of the variance explained in most of the GoM, but a few regions with more ~70% of the variance explained, and as observed in the amplitude and phase maps, this regions are localized in the slopes that lead to the deepest plains in the GoM. So, our modes seems to capture very well the variability associated to the slope bounded circulation patterns in the GoM.

![Maps of the proportional explained variance for the first 4 leading modes for the upper and deep layers](final_results/EV_maps_Nmodes4.png){#fig:frac-var-map width=85%}

## Discussion

In the original paper by [@olvera-prado_upperlower_2023], the author found that the firts 4 modes explains about 50% of total variance, with fractions of 23%, 12%, 8%, and 6% respectively, in figure ref{fig:amplitudes-phases-olvera} we can observe the amplitudes and phases of the first 4 modes found by [@olvera-prado_upperlower_2023], and in figure \ref{fig:frac-var-map-olvera} we can observe the maps of the explained variance for the first 4 modes found by [@olvera-prado_upperlower_2023]. Comparing our results with the original paper, we can observe that the the modes we recovered captures about the same amount of variance as the original paper.

Looking at the firts mode, we observe that the region of action for both modes is very similar, with the main difference being that the modes described in the original paper does not capture the coherent region in the northwestern and western part of the GoM, which is present in our mode, at the same time the amplitude in our modes is smaller than the one described in the original paper. When it comes to the phase analysis, we observe that the phases in the upper layer does not show a many coherent pattern with alternated directions as our modes, and the convergence region is located in the south as opposed to the one we found in our mode.

Some other similarities we can observe between our modes and the ones described in the original paper is that consistently we both observe high amplitude signals in the northen region around the 88W longitude in the lower layer, while we do not capture this responses in the same modes and with equivalent amplitude, we both observe that this region has a high importance in physical processes associated to the Loop Current System processes. In this same sense, mode 3 also exhibits a similar behaviors, in the upper layer we observe a strong response in the northwest region and also in the lower layer we observe a localized response in this same location in the lower layer, and in the original paper we also observe some signal in this same locations but the seem to be much weaker and more spread out, inparticular in the lower layer, were we observe a something that resembles more a slope trapped response in the north and west GoM.

Looking at the explained variance map, we can observe that explained variance in the upper layer is very well captured by the CEOF analysis, and it is very consistent with the results found by [@olvera-prado_upperlower_2023], However, the region of high explainability is much more spread to the west that in the original paper, however, in both cases we have very limited success on explaining the circulation in the southern portion of the GoM. When it comes to the deep layer, we are more successful on explaining the variability in the deep circulation, with some region reaching up to ~70% of the variance explained, that seem to be tied to the slope bounded circulation patterns in the GoM. Which as described by [@perez-brunius_dominant_2018], is one of the main circulation patterns in the deep GoM. So the CEOF analysis seems to do a decent job capturing the variability in the Gulf of Mexico and identify some possible couplings in the circulation patterns of the Gulf of Mexico.

![Amplitudes and Phases of the first 4 leading modes found by Olvera-Prado et al. (2023)](images/olvera_couppledmodes.png){#fig:amplitudes-phases-olvera width=75%}

![Maps of explained variance for the first 4 leading modes found by Olvera-Prado et al. (2023)](images/explained_vartiance.png){#fig:frac-var-map-olvera width=75%}

## Conclusion and Future Work

In this study we have analyzed the circulation in the Gulf of Mexico using the HYCOM model and the Complex Empirical Orthogonal Functions (CEOF) analysis. We have found that the firts 4 modes explain about 50% of the variance of the coupled upper-lower layer variability in the Gulf of Mexico, which is consistent with the results found by [@olvera-prado_upperlower_2023]. However, we have found that our analisys of deep circulation is very sensible to the depth isopicnal layer used as representative of the deep circulation, given that our analysis uses a deep layer from 1000 to 2000m depth which we expected to be a good approximation of the one used by [@olvera-prado_upperlower_2023], whyloe we succeded to identify some coherent patterns that seem to be similar to the ones described in the original paper, there is still needed to analyse more in depth the phases and amplitudes to get a better understanding of the deep circulation in the Gulf of Mexico. However, we the preliminar result found in this work suggest that there it might be possible to identify coupled patterns in the circulation since some of the recovered modes show similar spatial locations even if the are vertically isolated.

The found modes also seem to do a very good job on capturing the variability in the upper layer, with some regions reaching up to ~80% of the variance explained, while also explaining a significant amount of the variance in the deep layer, with some regions reaching up to ~70% of the variance explained. However, we still need to analyse the Principal Components (PC) to get a better understanding of the time scale dominances of the modes we found and identify if they follow temporal bounded cyclical patterns or they are also temporaly constant.

## References
