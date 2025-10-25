---
title: "Lab 2"
subtitle: "OCP 5050 Fall 2025"
author: "Jorge Eduardo Velasco Zavala"
date: "2025-10-22"
geometry: 
    - margin=1in
    - letterpaper
---

## Ekman Transport

The goal of this experiment demonstrated in this lab was to try to reproduce the Ekman Pumping phenomenon. To reproduce this process, we used a rotating tank with some fans blowing air in the surface layer of the tank, creating a flow that is parallel to the water surface, creating a stress, since the tank is rotating, the wind stress does not travel straight over the surface, it sufers a deflection effect, that creates a transport of water to the right of the wind flow directions. Lets look at the figure \ref{fig:ekman}.a, which show the general scheme of the convergence and downwelling of the water. In this case the direction of the rotation and the wind flow are in the same direction so the deflection effect points to the center of the tank, creating a convergence towards the center of the tank, which as consequence creates a downwelling pushing down the water in the center of the tank.

Now, if we look at the figure \ref{fig:ekman}.b,  we have the squeme of the case where the direction of the rotation and the wind flow are in the opposite direction, in this case the deflections still point to the right but since the wind flow is blowing right to left, the deflection effect points outward from the center of the tank, creating a divergence that push the water outward from the tank.

![General scheme of the ekman pumping experiment](images/ekman.jpg){#fig:ekman width=50%}

## Taylor Columns

The second experiment I want to discuss, is the Taylor Columns. To perform this exeriment, we first need to create a rotating fluid that behaves as a rigid body, so we need to make that the fluid behaves as a single body, and placing a solid obstacle in the in the bottom of the tank containing the fluid, in this case we used a hockey puck. Once the system reaches a steady solid body rotation, we add a some dye in the fluid as tracer to visualize the flow inside the fluid. The first thing we observe is that the dye won't move much in will remain in the same place relative to the tank, it will just extend to the bottom of the tank, this is an indication that the fluid is behaving as a rigid body, and that the rotation is not causing any shear in the fluid, so the dye won't spread around the tank, but show more a column of dye extending from the surface to the bottom of the tank.

The we dreceded the rotation of the tank a little bit in order to create a perturbation that pushes the dye forward and force to move towards the obstacle. The dye then will start to move toward the obstacle and instead of extending over the obstacle, it will move around it, while still advancing forward, see figure \ref{fig:taylor}, looking like courtines around the obstacle.

![Taylor Columns](images/taylor.jpg){#fig:taylor width=50%}

This is due to the fact that in a fluid that is rotating as a rigid body the horizontal velocity is constant, and therefore doesn't change with depth. So the dye will move around the obstacle at the same speed as the fluid is rotating, creating the observed pattern. This phenomenon is known as Taylor Columns and are explained by the Taylor-Proudman theorem, which states that in a fluid that is rotating as a rigid body the velocity along the rotation axis won't change with depth:

$$
(\Omega \cdot \nabla) \mathbf{u} = 0
$$

where $\Omega$ is the angular velocity of the fluid inside the tank, and $\mathbf{u}$ is the velocity of the fluid. In this case since the fluid is moving at constant velocity in all levels of depth, it looks like a 2D flow, so there are no vertical variations in the velocity:

$$
\frac{\partial u}{\partial z} = 0
$$

So, even when the puck is not as high as the surface of the fluid, the rotation is practically only occurring in the horizontal plane, so the dye will be pushed around the obstacle instead of going over it.

## Conclusions

During this lab we analyzed several experiment that help us to visually understand some processes that happen over the ocean in much larger scales. However, I just focused on two of them, the Ekman Pumping and the Taylor Columns.

In the Ekman Pumping experiment we demonstrated the effect of the wind stress on the ocean, and how due to this force the water is pushed to the right of the wind flow directions, in the northern hemisphere. This creates a net transport that creates a convergence towards the center and pushes the surface water to the depth and on the contrary, when we have situacion of divergence we push water from the depth to the surface.

In the Taylor Columns experiment we demonstrated the effect of the solid body rotation on the fluid, and how this creates a 2D flow pattern that pushes the flow around and obstacle. An effect that we can also observe in the ocean, and atmosphere, where the currents are pushed around topograpic obstacles like mountains.
