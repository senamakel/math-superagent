<!-- source: https://www.tec-science.com/mechanical-power-transmission/planetary-gear/transmission-ratios-of-planetary-gears-willis-equation/ | converted from HTML -->

Transmission ratios of planetary gears (Willis equation) | tec-science

**

**[Youtube][1]

**

- [image: Deutsch] [2]
- [image: English] [3]
- [Home][4]
- **[Mechanics][5]

  - [Gases and liquids][6]

- **[Chemistry][7]

  - [Structure of matter][8]
  - [Atomic models][9]
  - [Chemical bonds][10]

- **[Material science][11]

  - [Structure of metals][12]
  - [Ductility of metals][13]
  - [Solidification of metals][14]
  - [Alloys][15]
  - [Steelmaking][16]
  - [Iron-carbon phase diagram][17]
  - [Heat treatment of steels][18]
  - [Material testing][19]

- **[Mechanical power transmission][20]

  - [Basics][21]
  - [Gear types][22]
  - [Belt drive][23]
  - [Planetary gear][24]
  - [Involute gear][25]
  - [Cycloidal gear][26]

- **[Thermodynamics][27]

  - [Temperature][28]
  - [Kinetic theory of gases][29]
  - [Heat][30]
  - [Thermodynamic processes in closed systems][31]
  - [Thermodynamic processes in open systems][32]

- **[Optics][33]

  - [Geometrical optics][34]

**

Sign in

Welcome! Log into your account

Forgot your password? Get help

[Privacy Policy][35]

Password recovery

Recover your password

A password will be e-mailed to you.

[image: logo tec-science] [tec-science][4]

**

[image: logo tec-science] [4][image: logo tec-science] [4]

- [image: Deutsch] [2]
- [image: English] [3]
- [Home][4]
- [Mechanics][5]

  - [Gases and liquids][6]

- [Chemistry][7]

  - [Structure of matter][8]
  - [Atomic models][9]
  - [Chemical bonds][10]

- [Material science][11]

  - [Structure of metals][12]
  - [Ductility of metals][13]
  - [Solidification of metals][14]
  - [Alloys][15]
  - [Steelmaking][16]
  - [Iron-carbon phase diagram][17]
  - [Heat treatment of steels][18]
  - [Material testing][19]

- [Mechanical power transmission][20]

  - [Basics][21]
  - [Gear types][22]
  - [Belt drive][23]
  - [Planetary gear][24]
  - [Involute gear][25]
  - [Cycloidal gear][26]

- [Thermodynamics][27]

  - [Temperature][28]
  - [Kinetic theory of gases][29]
  - [Heat][30]
  - [Thermodynamic processes in closed systems][31]
  - [Thermodynamic processes in open systems][32]

- [Optics][33]

  - [Geometrical optics][34]

**[Youtube][1]

****

[Home][4]**[Mechanical power transmission][36]**[Planetary gear][24]**Transmission ratios of planetary gears (Willis equation)

**

Learn more about the derivation of the different transmission ratios of planetary gears in this article.

## Willis equation for planetary gears

In the article [Willis equation for planetary gears][37], the following fundamental equation was derived describing the motion of sun gear (s), ring gear (r) and carrier (c) of a planetary gear:

\begin{align}
\label{pl}
&\boxed{n_r \cdot z_r = n_c \cdot \left(z_r + z_s \right) – z_s \cdot n_s} \\[5px]
\end{align}

In this equation, n denotes the rotational speed of the components and z the number of teeth of the respective gears. This equation can now be used to show the different transmission ratios of planetary gears.

[image: Planetary gear] Figure: Planetary gear

## Transmission ratios

With a single planetary gear set one will obtain three different modes of operation, depending on which component (sun gear, carrier or ring gear) is fixed. Input and output are then carried out by the other two components. Which transmission ratios result in each case, is shown in the next section.

Animation: Operating modes of planetary gears

### Fixed sun gear

If the sun gear is fixed (n s =0) and the gearbox input is carried out by the ring gear and the output by the carrier, the following transmission ratio i s =n r /n c results according to equation (\ref{pl}):

\begin{align}
&n_r \cdot z_r = n_c \cdot \left(z_r + z_s \right) – z_s \cdot \underbrace{n_s}_{=0} \\[5px]
&n_r \cdot z_r = n_c \cdot \left(z_r + z_s \right) \\[5px]
&\frac{n_r}{n_c} = i_s = \frac{z_r+z_s}{z_r} \\[5px]
\label{i_s}
&\boxed{i_s = 1+\frac{z_s}{z_r}} ~~~1<i_s<2 \\[5px]
\end{align}

Equation (\ref{i_s}) shows that the transmission ratio is always greater than 1, i.e. the rotational speed is decreased by the planetary gearbox. But the transmission ratio is also limited to a maximum value, since the number of teeth of the sun gear must always be smaller than that of the ring gear (otherwise the sun gear would be larger than the surrounding ring gear). In the theoretical limiting case, if the sun gear is as large as the ring gear and therefore both have identical numbers of teeth, the teeth ratio becomes z s /z r =1 and the transmission ratio 2 at most.

If input and output are reversed, i.e. the gearbox input is carried out by the carrier and the output by the ring gear, then the transmission ratio range lies between 1 and 0.5.

### Fixed ring gear

A further possibility for speed conversion is obtained, when the ring gear is fixed (n r =0) and the gearbox input is carried out by the sun gear and the output by the carrier. This results in the following transmission ratio i r =n s /n c:

\begin{align}
&\underbrace{n_r}_{=0} \cdot z_r = n_c \cdot \left(z_r + z_s \right) – z_s \cdot n_s \\[5px]
&0 = n_c \cdot \left(z_r + z_s \right) – z_s \cdot n_s \\[5px]
&\frac{n_s}{n_c} = i_r = \frac{z_r+z_s}{z_s} \\[5px]
\label{i_r}
&\boxed{i_r = 1+\frac{z_r}{z_s}} ~~~2<i_r<\infty \\[5px]
\end{align}

Animation: Planetary gear with fixed ring gear

In the present case one also obtains a reduced rotational speed, because the transmission ratio will be greater than 2 in any case, since the number of teeth of the ring gear is always greater than that of the sun gear [the teeth ratio is thus greater than 1 (z r /z s >1)]. The transmission ratio is not limited to a maximum value, since the ring gear and thus its number of teeth can in principle be chosen as large as desired and the transmission ratio then strives towards infinity.

If, in the opposite case, the gearbox input is no longer carried out by the carrier but by the ring gear, then the reciprocal transmission ratios with a range between 0 and 0.5 are obtained.

### Fixed carrier

A last possibility for the transmission ratio is obtained when the carrier ist fixed and the gearbox input is carried out by the sun gear and the output by the ring gear. In this case the following transmission ratio i 0 =n s /n r results:

\begin{align}
&n_r \cdot z_r = \underbrace{n_c}_{=0} \cdot \left(z_r + z_s \right) – z_s \cdot n_s \\[5px]
&n_r \cdot z_r = – z_s \cdot n_s \\[5px]
&\frac{n_s}{n_r} = i_0 = -\frac{z_r}{z_s} \\[5px]
\label{i_0}
&\boxed{i_0 = -\frac{z_r}{z_s}} ~~~\text{“stationary transmission ratio”}~~~-\infty<i_0<-1 \\[5px]
\end{align}

Animation: Planetary gear with fixed carrier

First of all, the negative sign is noticeable in the transmission ratio of equation (\ref{i_0}). It indicates that the direction of rotation between input and output shaft changes (“reverse gear”). In the present case, the transmission ratio ranges between -∞ and -1 and in the opposite case (when input and output are reversed) between -1 and 0.

Note, that in this case the planetary gear works like a [stationary gearbox][38] without moving rotational axes. For this reason, the transmission ratio in the case of a fixed carrier also called *fixed carrier transmission ratio*or *stationary transmission ratio*i 0!

### Direct drive

A planetary gear can also be used as a so-called *direct drive*. The carrier and the sun gear are firmly fixed to the ring gear. In this case, the rotary motion is transmitted directly from the input shaft to the output shaft (transmission ratio 1:1). Such a direct drive is used, for example, in [three-speed gear hubs][39] as the “2nd gear”.

Animation: Planetary gear with direct drive

### Stationary transmission ratio (fixed carrier transmission ratio)

If one looks at the equations (\ref{i_s}), (\ref{i_r}) and (\ref{i_0}), then obviously all transmission ratios can also be expressed by the *fixed carrier transmission ratio*i 0 =-z r /z s. For a fixed sun gear, the transmission ratio i s then becomes:

\begin{align}
&\boxed{i_s = 1-\frac{1}{i_0}} \\[5px]
\end{align}

For a fixed ring gear, the transmission ratio i r can be calculated as follows using the *fixed carrier transmission ratio*i 0:

\begin{align}
&\boxed{i_r = 1-i_0}\\[5px]
\end{align}

Even the fundamental equation for planetary gears (\ref{pl}) can be expressed by the *fixed carrier transmission ratio*i 0:

\begin{align}
&n_r \cdot z_r = n_c \cdot \left(z_r + z_s \right) – z_s \cdot n_s \\[5px]
&n_r \cdot \frac{z_r}{z_s} = n_c \cdot \left( \frac{z_r}{z_s} + 1 \right) – n_s \\[5px]
& – n_r \cdot i_0 = n_c \cdot \left(1-i_0 \right) – n_s \\[5px]
&\boxed{ n_s = n_c \cdot \left(1-i_0 \right) + n_r \cdot i_0 }~~~\text{with}~~~\boxed{i_0=-\frac{z_r}{z_s}}~~~\text{fixed carrier transmission ratio} \\[5px]
\end{align}

#### RELATED ARTICLES MORE FROM AUTHOR

[image: Velocity distribution on the rotating planet gear with moving carrier] [37]

[Planetary gear][24]

### [Willis equation for planetary gears][37]

[image: Exploded view of a cycloidal drive] [40]

[Planetary gear][24]

### [How does a cycloidal drive work?][40]

[image: Design of the cycloidal disc with an ordinary cycloid] [41]

[Planetary gear][24]

### [Construction of the cycloidal disc of a cycloidal drive][41]

[image: 5th step - symmetrical arrangement of the bevel gears to avoid bending stresses] [42]

[Planetary gear][24]

### [How does a differential gear work?][42]

[image: Carrier of a three-speed gear hub] [43]

[Planetary gear][24]

### [How does a three-speed gear hub work?][43]

[image: Relationship between the pitch circle diameters and the number of teeth] [44]

[Planetary gear][24]

### [Derivation of Willis equation (fundamental equation of planetary gears)][44]

****

[image: logo tec-science] [4]

**[Youtube][1]

- [Legal notice][45]
- [Privacy Policy][35]

&copy; Copyright 2025 tec-science

This website uses cookies. If you continue to use this website, we will assume your consent and we will only use personalized ads that may be of interest to you. As long as your consent is not given, no ads will be displayed. More information about this in the privacy policy. Accept Refuse [Privacy Policy][35]


## Links

[1]: https://www.youtube.com/@tec-science
[2]: https://www.tec-science.com/de/getriebe-technik/planetengetriebe/ubersetzungsmoglichkeiten-der-plantengetriebe/
[3]: https://www.tec-science.com/mechanical-power-transmission/planetary-gear/transmission-ratios-of-planetary-gears-willis-equation/
[4]: https://www.tec-science.com/
[5]: https://www.tec-science.com/mechanics/
[6]: https://www.tec-science.com/category/mechanics/gases-and-liquids/
[7]: https://www.tec-science.com/chemistry/
[8]: https://www.tec-science.com/category/chemistry/structure-of-matter/
[9]: https://www.tec-science.com/category/chemistry/atomic-models/
[10]: https://www.tec-science.com/category/chemistry/chemical-bonds/
[11]: https://www.tec-science.com/material-science/
[12]: https://www.tec-science.com/category/material-science/structure-of-metals/
[13]: https://www.tec-science.com/category/material-science/ductility-of-metals/
[14]: https://www.tec-science.com/category/material-science/solidification-of-metals/
[15]: https://www.tec-science.com/category/material-science/alloys/
[16]: https://www.tec-science.com/category/material-science/steel-making/
[17]: https://www.tec-science.com/category/material-science/iron-carbon-phase-diagram/
[18]: https://www.tec-science.com/category/material-science/heat-treatment-steel/
[19]: https://www.tec-science.com/category/material-science/material-testing/
[20]: https://www.tec-science.com/mechanical-power-transmission/
[21]: https://www.tec-science.com/category/mechanical-power-transmission/basics/
[22]: https://www.tec-science.com/category/mechanical-power-transmission/gear-types/
[23]: https://www.tec-science.com/category/mechanical-power-transmission/belt-drive/
[24]: https://www.tec-science.com/category/mechanical-power-transmission/planetary-gear/
[25]: https://www.tec-science.com/category/mechanical-power-transmission/involute-gear/
[26]: https://www.tec-science.com/category/mechanical-power-transmission/cycloidal-gear/
[27]: https://www.tec-science.com/thermodynamics/
[28]: https://www.tec-science.com/category/thermodynamics/temperature/
[29]: https://www.tec-science.com/category/thermodynamics/kinetic-theory-of-gases/
[30]: https://www.tec-science.com/category/thermodynamics/heat/
[31]: https://www.tec-science.com/category/thermodynamics/thermodynamic-processes-in-closed-systems/
[32]: https://www.tec-science.com/category/thermodynamics/thermodynamic-processes-in-open-systems/
[33]: https://www.tec-science.com/optics/
[34]: https://www.tec-science.com/category/optics/geometrical-optics/
[35]: https://www.tec-science.com/privacy-policy/
[36]: https://www.tec-science.com/category/mechanical-power-transmission/
[37]: https://www.tec-science.com/mechanical-power-transmission/planetary-gear/willis-equation-for-planetary-gears/
[38]: https://www.tec-science.com/mechanical-power-transmission/planetary-gear/epicyclic-planetary-gear/
[39]: https://www.tec-science.com/mechanical-power-transmission/planetary-gear/three-speed-internal-gear-hub/
[40]: https://www.tec-science.com/mechanical-power-transmission/planetary-gear/how-does-a-cycloidal-gear-drive-work/
[41]: https://www.tec-science.com/mechanical-power-transmission/planetary-gear/construction-of-the-cycloidal-disc/
[42]: https://www.tec-science.com/mechanical-power-transmission/planetary-gear/how-does-a-differential-gear-work/
[43]: https://www.tec-science.com/mechanical-power-transmission/planetary-gear/how-does-a-three-speed-gear-hub-work/
[44]: https://www.tec-science.com/mechanical-power-transmission/planetary-gear/fundamental-equation-of-planetary-gears-willis-equation/
[45]: https://www.tec-science.com/disclaimer/
