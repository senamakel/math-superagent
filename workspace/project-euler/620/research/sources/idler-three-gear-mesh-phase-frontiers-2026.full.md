<!-- source: https://www.frontiersin.org/journals/mechanical-engineering/articles/10.3389/fmech.2026.1721474/full | converted from HTML -->

Frontiers | Contact dynamics modeling of a three-gear system and vibration characteristics analysis of the idler gear

## ORIGINAL RESEARCH article

Front. Mech. Eng., 31 July 2026

Sec. Vibration Systems

Volume 12 - 2026 | [https://doi.org/10.3389/fmech.2026.1721474][1]

# Contact dynamics modeling of a three-gear system and vibration characteristics analysis of the idler gear

-

[Z Y Zhiwei You 1,2 *][2]
-

[Y L Yuankui Luo 3][3]
-

L X

Lixin Xu 3

-

-

1. College of Mechanical and Electrical Engineering, Central South University, Changsha, China

-

2. AECC Hunan Aviation Powerplant Research Institute, Zhuzhou, China

-

3. State Key Laboratory of Mechanical Transmission for Advanced Equipment, Chongqing University, Chongqing, China

- See more

Article metrics

View details

## Abstract

The idler gear is a transitional component in a gear transmission system. By meshing with two non-contacting gears, it changes the rotation direction of the driven gear while maintaining the original transmission ratio. Based on the theories of contact dynamics and multibody dynamics, this paper establishes a contact dynamics model for a three-gear system, which consists of two components: a tooth profile mathematical model and a contact dynamics model. In the tooth profile mathematical model, the meshing phase angle must be calculated to satisfy the initial assembly relationships. In the contact dynamics model, a 9DoF dynamic differential equation for the three-gear system needs to be established, and a contact model for the three-gear system should be constructed based on the mathematical contact judgment method derived from previous research. Based on the established model, this paper investigates the dynamic responses of two-gear and three-gear systems under varying input speeds and load torques. By comparing these results, the influence of the idler gear on the vibration characteristics of the three-gear system is analyzed. The proposed model and findings provide useful reference for the design of idler gears in gear transmission systems.

## 1 Introduction

As the core power transmission component of modern industrial equipment, gear transmission systems directly affect the service performance of the transmission system. In three-gear systems, the idler gear, as an intermediate transmission unit, not only undertakes load transmission but also exhibits unique asymmetric support characteristics, which are prone to induce vibrations and noise, thereby affecting the equipment’s service lifespan.

Numerous scholars have conducted systematic studies on gear system dynamics, and the commonly used modeling methods primarily include the analytical method ( Autiero et al., 2024; Wang and Parker, 2022; Yuan et al., 2025; Hu et al., 2025; Eritenel and Parker, 2012; Portron and Marques, 2025; Samani et al., 2019; Tamarozzi et al., 2013), finite element method ( Thunuguntla et al., 2025; Ding et al., 2022; Zhang X. et al., 2025; Ramamurti et al., 1998; Abousleiman and Velex, 2006; Kong et al., 2023), and experimental method ( Ericson and Parker, 2013; Zhang T. et al., 2025; Singh et al., 2008; Schlegel and Mard, 1967; Toda and Botman, 1979).

Using the aforementioned methods, numerous scholars have conducted research on idler gears. Li et al. (2023a) investigated a helical idler gear system, considering two key factors: the number of idler gear teeth and the angle between gear centerlines to study how phase configuration relationships impact the system’s dynamic characteristics. Arian and Taghvaei (2021) investigated the chaotic dynamics of a spur gear system with an idler gear. By developing a nonlinear dynamic model incorporating backlash and time-varying stiffness, they revealed the influence of the idler gear on the paths to chaos. Yu and Xu (2006) conducted a failure analysis on a 20CrMnTi steel plasma-carburized idler gear in a truck diesel engine gearbox, revealing that cracks originated from the root fillet area of the spline inner ring welding zone. Rook and Singh (1995) focused on a reverse idler gear system within a multi-degree-of-freedom mechanical system as a representative case, specifically investigating concurrent nonlinear issues induced by vibrations and impacts under light load conditions. Xu et al. (2011) developed a four-gear multi-rigid-body dynamic model for the power-driven turntable idler gear system, analyzing its vibration modal frequencies and mode shapes. Li et al. (2023b) investigated the helical idler gear system under high-speed and heavy-duty conditions, developing a dynamic model of bending fatigue failure encompassing three stages (intact, cracked, and broken-tooth) to specifically reveal the failure evolution mechanisms of the idler gear and input gear. Focusing on the idler gear drive system, Li et al. (2024) developed a dynamic fault model for helical gears that incorporates center distance deviations and angular misalignments, demonstrating how idler shaft positional errors govern vibration patterns in the system. Li and Wang (2011) proposed an over constrained scaling mechanism based on gear pairs, whose fundamental unit comprises small gears mounted at the ends of two connecting rods and an idler gear. Ding et al. (2024) proposed an electric drive wheel (EDW) integrated with an idler gear, combining power transmission and suspension functions. Their study focused on analyzing the geometric constraints of the idler gear configuration and its impact on the longitudinal and vertical dynamic characteristics of the system. Liu and Parker (2008) focused on the nonlinear parametric excitation dynamics of the idler gear set, revealing the coupling characteristics between parametric excitation and tooth separation induced by double meshing points. Fakhfakh et al. (2015) developed a multi-stage helical idler gear torsional dynamic model using the base surface contact line discretization method. They incorporated time-varying mesh stiffness and initial backlash to characterize tooth profile deviations and solved the nonlinear system by integrating the Newmark algorithm with a normal contact algorithm. Houser et al. (2002) targeted an aircraft idler gearbox, analyzing transient acceleration noise data through Vold-Kalman filtering, and comparing two types of idler dynamic models: jump-type and continuous-parameter.

Previous studies on idler gear system dynamics have primarily relied on traditional lumped parameter methods and finite element methods (FEM). These two approaches exhibit distinct trade-offs: the lumped parameter method offers high computational efficiency but lower accuracy, while FEM provides high precision at the cost of computational intensity. Building on earlier research ( Luo and Xu, 2025; Xu et al., 2024), this paper establishes a three-gear contact dynamics model that directly characterizes the power transmission process of the idler gear. By comparing the vibrational characteristics of two-gear and three-gear systems, we investigate the influence of the idler gear on the dynamic response of the three-gear system.

The main innovation of this paper lies in proposing a mathematical contact determination method tailored for three-gear systems, which characterizes the geometric features of the three gears using mathematical expressions, thereby transforming the contact problem into solving a system of equations.

## 2 Mathematical modeling of tooth profiles for a three-gear system

The three-gear system comprises the input gear (power input), the idler gear (power transmission), and the output gear (power output).

The involute mathematical models of the input gear, the idler gear, and the output gear can be constructed with reference to Xu et al. (2024). The mathematical expressions for the left and right involute tooth profiles of each gear in the three-gear system are derived as: where, the superscript (*l*) denotes the *l*th gear in the three-gear system, with the input gear corresponding to *l*= 1, the idler gear to *l*= 2, and the output gear to *l*= 3. Subsequent superscripts (*l*) follow the same convention. Definitions of other variables refer to Xu et al. (2024).

Following the method in Xu et al. (2024), the input gear is rotated by according to the initial tooth mathematical model for the pinion, while the idler gear and the output gear are rotated by and based on the initial tooth mathematical model for the gear. The values of , and are calculated as per Xu et al. (2024).

To ensure proper meshing alignment in the three-gear system, the tooth profiles constructed in the previous step must be rotated to their initial positions. The initial position of the three-gear system is illustrated as shown in Figure 1.

FIGURE 1

[image: Labeled diagram showing three gears: input gear at O1, idler gear at O2, and output gear at O3, each with labeled base circles and coordinate axes. Arrows and angles Î¸12 and Î¸23 indicate rotation directions and mesh orientations.]

The initial position of the three-gear system.

In the gear position shown in Figure 1, first assemble the input gear and the idler gear according to the illustrated positions. Both the input gear and the idler gear must be rotated by an angle . Then, position the output gear as depicted in the figure, requiring it to be rotated by an angle . Note that the values of and carry sign conventions: angles in the first quadrant of the coordinate system are assigned positive values, while those in the fourth quadrant are assigned negative values.

To satisfy the meshing alignment between the idler gear and the output gear, the tooth currently positioned on the O 1 O 2 line in the idler gear must be rotated to the location marked by the dashed line. The required rotation angle for the idler gear is:

In the gear system assembly shown in Figure 1, the idler gear has an odd number of teeth. However, when the idler gear has an even number of teeth, the required rotation angle differs, as illustrated in Figure 2 for varying tooth count configurations. For an even number of teeth , an additional rotation angle must be applied to the idler gear. The required rotation angle in this case is:

FIGURE 2

[image: Diagram showing two cases of input and idle gear interactions. Both panels, labeled (a) and (b), depict two base circles with axes, one for each gear, labeled O1 and O2. Arrows indicate coordinate axes y1, y2, and x. The left gear is labeled input gear, the right is labeled idle gear. Panel (a) shows opposing purple rotation arrows on the gears, while panel (b) shows parallel rotation arrows, illustrating different rotational directions. Both diagrams emphasize the interaction at the gear interface.]

Meshing configurations for different tooth counts: **(a)**odd number of teeth, **(b)**even number of teeth.

At this point, the corresponding gear teeth on the idler gear will align along the O 1 O 2 centerline. Meanwhile, the input gear, which meshes with the idler gear, must rotate by an angle , where represents the transmission ratio between the input gear and the idler gear.

Based on the above analysis, the rotation angles required for each gear in the three-gear system to return to their initial positions are:

The initial tooth profile mathematical model of the input gear is:

The initial tooth profile mathematical model of the idler gear is:

The initial tooth profile mathematical model of the output gear is:

By performing a circular array of the obtained initial tooth profiles, the complete tooth profile mathematical expressions for the three-gear system are: where, *i*= 1, 2, … , , denotes the *i*th tooth of the gear, is the number of teeth of the *l*th gear, and are the center coordinates of the *l*th gear.

## 3 Construction of contact dynamics model for three-gear system

The mathematical model of the three-gear system is the key to transforming the geometric problem of the gear system into a mathematical problem, and also serves as the foundation for contact determination in the contact dynamic model.

In the three-gear system, the idler gear simultaneously meshes with both the input gear and the output gear. When all three gears are standard involute gears, the system exhibits two contact scenarios. Case 1: the left-side involute profile of the input gear meshes with the left-side involute of the idler gear, while the right-side involute of the idler meshes with the right-side involute of the output gear. Case 2: the right-side involute of the input gear meshes with the right-side involute of the idler gear, and the left-side involute of the idler meshes with the left-side involute of the output gear. Figure 3 illustrates the 9 DoF dynamic model of the three-gear system.

FIGURE 3

[image: Technical illustration showing two labeled gear train diagrams, each with input, idle, and output gears, directional arrows, force vectors, and coordinate axes, highlighting the transmission paths and mechanical interactions between gears.]

The 9DoF dynamic model of the three-gear system: **(a)**the input gear rotates counterclockwise, **(b)**the input gear rotates clockwise.

According to the model shown in Figure 3, the generalized coordinates of the three-gear system are expressed as a vector:

Based on the 9DoF dynamic model of the three-gear system, the dynamic differential equations are formulated as: where, is the mass of the *l*th gear, is the moment of inertia of the *l*th gear, *g*is the gravitational acceleration, and are the resultant forces of elastic and damping forces in the *x*- and *y*-directions for the *l*th gear, and (*j*= 1, 2, 3, … , 7, 8) represent the forces in the *x*- and *y*-directions at the *j*th meshing point of the *l*th gear, denotes the resultant external torque at the respective gear center due to the forces at the *j*th meshing point, is the driving torque, and is the load torque.

The Runge-Kutta method is employed to solve Equation 12, and the initial conditions for the solution are: where, , and denote the required rotational angular velocities of the three-gear system.

The position and velocity of the three-gear system for the next cycle are obtained as:

Then, the profile expression of the three-gear system in the *k*th cycle is updated as:

The meshing line equation in Figure 3 is given as: where, denotes the slope of the *n*th meshing line, and represents the node coordinates at the *n*th meshing line. Specifically, corresponds to , to , to , and to .

Simultaneously solving Equations 15, 16 yields the coordinates of the intersection points between the tooth profile and the meshing line. On the same meshing line, two distinct gears generate intersection points, respectively. The distance between adjacent intersection points on different profiles represents the infinitesimal penetration in the penalty method. Consequently, the normal contact force at this location is calculated as: where, is the TVMS, is an exponent determined by the material properties of the body, and is the damping coefficient, which is calculated by the following formula: where, and denote the pinion and the gear, respectively; and represent the rotational inertias of the pinion and gear about their own rotational centers; and are the pitch radii of the pinion and gear; is the mean meshing stiffness, and is the meshing damping ratio.

The local friction force is expressed as: where, is the coefficient of friction, is the tangential relative velocity, and is the friction parameter.

The contact force and friction force are projected onto the *x*-axis and *y*-axis to obtain the components and in the equation. Subsequently, the resultant external moment can be calculated based on these forces and the contact point coordinates.

The bearing support force is calculated by the following equation: where, and denote the elastic coefficient and damping coefficient, respectively. They are calculated as follows: where, is the support damping ratio; is the roller diameter, is the bearing radial load, is the number of rollers, and is the contact angle.

## 4 Results and discussion

Based on the constructed model, the effects of different input speeds and load torques on the dynamic responses of the two-gear and three-gear systems are investigated. The two-gear system model refers to the literature ( Xu et al., 2024). The parameters of the two-gear and three-gear systems are shown in Table 1. The specific operating conditions are detailed in Table 2. Table 3 lists the dynamic parameters and Table 4 lists the geometric parameters.

TABLE 1

Gear system | Gear type | Module (mm) | Number of teeth | Pressure angle | Tooth width (mm) | Addendum coefficient (mm) | Clearance coefficient (mm) |

Two-gear system | Input gear | 2 | 30 | 20° | 10 | 1 | 0.25 |

Output gear | 2 | 120 | 20° | 10 | 1 | 0.25 |

Three-gear system | Input gear | 2 | 30 | 20° | 10 | 1 | 0.25 |

Idler gear | 2 | 60 | 20° | 10 | 1 | 0.25 |

Output gear | 2 | 120 | 20° | 10 | 1 | 0.25 |

The parameters of two-gear and three-gear systems.

TABLE 2

No. | Input speed (rpm) | Load torque (N∙m) |

1 | 600 | 50 |

2 | 1,000 | 50 |

3 | 1,000 | 5 |

4 | 1,000 | 100 |

The specific operating conditions.

TABLE 3

Parameter | Value | Unit |

Young’s modulus |  | Pa |

Poisson’s ratio | 0.3 | - |

Density | 7,800 | kg/m 3 |

Friction coefficient | 0.02 | - |

Mass of the input gear | 0.2426 | kg |

Mass of idler gear | 0.7057 | kg |

Mass of the output gear | 3.1758 | kg |

Moment of inertia of the input gear |  | kg·m 2 |

Moment of inertia of idler gear | 0.0013 | kg·m 2 |

Moment of inertia of the output gear | 0.0229 | kg·m 2 |

The dynamic parameters.

TABLE 4

Gear system | Gear type | Pitch diameter (mm) | Outside diameter (mm) | Root diameter (mm) |

Two-gear system | Input gear | 60 | 64 | 55 |

Output gear | 240 | 244 | 235 |

Three-gear system | Input gear | 60 | 64 | 55 |

Idler gear | 120 | 124 | 115 |

Output gear | 240 | 244 | 235 |

The geometric parameters.

### 4.1 Dynamic response of two-gear and three-gear systems under different input speeds

When the load torque is 50 N∙m, the dynamic responses of the two-gear and three-gear systems under input speeds of 600 rpm and 1,000 rpm are investigated. As shown in Figures 4, 5 the dynamic response of the output gear in the two-gear system under different input speeds is illustrated.

FIGURE 4

[image: Panel (a) shows an orange time-series line graph of acceleration in the x-direction from approximately -25 to 15 meters per second squared versus time from 0.02 to 0.1 seconds, with labeled mesh in and out points and marked periods. Panel (b) presents a blue bar chart of acceleration amplitude versus frequency from zero to ten kilohertz, highlighting peaks at integer multiples of a fundamental frequency labeled from f_m to 10f_m.]

The dynamic response of the output gear in the two-gear system under an input speed of 600 rpm: **(a)**time domain, **(b)**frequency domain.

FIGURE 5

[image: Panel a shows an orange acceleration waveform versus time with marked peaks, labeled coordinates, and noted periods and time intervals. Panel b presents a blue frequency spectrum with labeled harmonics, showing tallest peak at 2f_m1 and multiple additional harmonics labeled up to 10f_m1.]

The dynamic response of the output gear in the two-gear system under an input speed of 1,000 rpm: **(a)**time domain, **(b)**frequency domain.

In Figures 4a, 5a, the vibration acceleration of the two-gear system under different input speeds exhibits periodic characteristics. When the input speed is 600 rpm, the vibration period is 0.00333 s, which corresponds to the time interval between the meshing of consecutive teeth, calculated as 1/f m, where f m is the meshing frequency of the gear system at 600 rpm. The time interval between the meshing-out of one tooth and the meshing-in of the next is 0.00075 s, denoted as . When the input speed increases to 1,000 rpm, the vibration acceleration period becomes 1/f m1 = 0.002 s, where f m1 is the meshing frequency at 1,000 rpm. The time interval between the meshing-out of one tooth and the meshing-in of the next is . In Figures 4b, 5b, the frequency components of vibration acceleration under different speeds are dominated by the meshing frequency and its harmonics, primarily concentrated in the lower-order multiples.

By comparing the vibration acceleration of the output gear in the two-gear system with that of the output gear in the three-gear system, the influence of the idler gear on the vibration acceleration characteristics of the gear system is studied. The dynamic response of the output gear in the three-gear system under different rotational speeds is shown in Figures 6, 7.

FIGURE 6

[image: Panel a is a line graph showing acceleration in meters per second squared versus time in seconds, with repeated sharp peaks and annotated points marking mesh in and mesh out events. Panel b is a bar graph of acceleration versus frequency in thousands of hertz, showing labeled harmonic peaks at integer multiples of a base frequency fm.]

The dynamic response of the output gear in the three-gear system under an input speed of 600 rpm: **(a)**time domain, **(b)**frequency domain.

FIGURE 7

[image: Panel a shows a time-domain plot of acceleration in meters per second squared versus time in seconds with labeled mesh in and mesh out points. Panel b displays a frequency-domain plot with labeled harmonics of the primary frequency component.]

The dynamic response of the output gear in the three-gear system under an input speed of 1,000 rpm: **(a)**time domain, **(b)**frequency domain.

In Figures 6a, 7a, the vibration acceleration under different rotational speeds remains periodic, with time intervals consistent with those observed in the two-gear system. The peak-to-peak vibration acceleration of the output gear in the three-gear system is 37 m/s 2 and 42 m/s 2 at 600 rpm and 1,000 rpm, respectively; while that in the two-gear system is 33 m/s 2 and 36 m/s 2 under the same operating conditions. Due to the influence of the idler gear, the peak-to-peak vibration acceleration of the output gear in the three-gear system is significantly larger, and the transient fluctuations in acceleration are more frequent. The time interval between the meshing-out of one tooth and the meshing-in of the next is only approximately equal to the theoretical interval, unlike the two-gear system, where this interval aligns precisely with theoretical predictions. In Figures 6b, 7b, the frequency components of vibration acceleration are dominated by the meshing frequency and its harmonics. However, compared to the two-gear system, where vibration energy is concentrated in the lower-order harmonics, the energy distribution in the three-gear system spans a broader range, primarily between f m ∼10f m.

In the three-gear system, although the idler gear bears no external load, it transmits power from the input gear to the output gear while being dynamically influenced by both gears. The dynamic response of the idler gear under different rotational speeds is illustrated in Figures 8, 9.

FIGURE 8

[image: Panel (a) shows an orange acceleration waveform over time with several marked data points, intervals, and mesh positions labeled with corresponding times and coordinates. Panel (b) displays a frequency spectrum of acceleration featuring distinct harmonic peaks labeled from f sub m to 10 f sub m, along the x-axis ranging from zero to ten thousand hertz.]

The dynamic response of the idler gear under an input speed of 600 rpm: **(a)**time domain, **(b)**frequency domain.

FIGURE 9

[image: Panel (a) shows a time-domain graph of acceleration versus time with annotations highlighting mesh in and mesh out points, specific coordinates, and time intervals. Panel (b) displays a frequency-domain spectrum of acceleration with labeled harmonic peaks at integer multiples of base frequency f_m1, illustrating periodic signal characteristics.]

The dynamic response of the idler gear under an input speed of 1,000 rpm: **(a)**time domain, **(b)**frequency domain.

In Figures 8a, 9a, the vibration acceleration period of the idler gear under different speeds remains 0.00333 s at 600 rpm and 0.002 s at 1,000 rpm. The peak-to-peak vibration acceleration of the idler gear in the three-gear system is 347 m/s 2 and 305 m/s 2 at 600 rpm and 1,000 rpm, respectively. Since the idler gear is simultaneously influenced by both the input gear and the output gear, its peak-to-peak vibration acceleration is considerably large, reaching approximately 9.37 times and 7.26 times that of the output gear in the three-gear system at 600 rpm and 1,000 rpm, respectively. The transient fluctuations in acceleration are more frequent. Two distinct time intervals between the meshing-out of one tooth and the meshing-in of the next are observed: one caused by the meshing impacts between the input gear and the idler gear, and the other by those between the output gear and the idler gear. In Figures 8b, 9b, the frequency components of vibration acceleration are dominated by the meshing frequency and its harmonics, but the vibration energy is primarily concentrated around 8f m.

To further investigate the vibration enhancement mechanism induced by the idler gear, the instantaneous mesh-in and mesh-out states of the gear system are analyzed. The abrupt change in vibration acceleration occurring at 0.0183 s in Figure 9a is caused by the mesh-out of the input gear, and the instantaneous state of the gear system at this moment is illustrated in Figure 10. In the figure, the blue arrows represent the normal contact forces, while the red arrows denote the friction forces. At this instant, only one pair of teeth is in contact between the input gear and the idler gear, whereas the contact between the output gear and the idler gear remains in a double-tooth contact state.

FIGURE 10

[image: Technical diagram features two interlocking gear shapes, one large circular gear with fine teeth and one smaller, irregularly shaped gear to the left, both outlined in colored lines over a grid background.]

Instantaneous state of the input gear at mesh-out.

The abrupt change in vibration acceleration occurring at 0.01865 s in Figure 9a is caused by the mesh-in of the input gear, and the instantaneous state of the gear system at this moment is illustrated in Figure 11. In the figure, the blue arrows represent the normal contact forces, while the red arrows denote the friction forces. At this instant, both the input gear and the idler gear, as well as the output gear and the idler gear, are in a double-tooth contact state.

FIGURE 11

[image: Engineering diagram of two gears in mesh, one large and one small, with detailed tooth profiles in orange, green, and pink, overlaid with blue and red lines indicating contact points and axes.]

Instantaneous state of the input gear at mesh-in.

The abrupt change in vibration acceleration occurring at 0.01916 s in Figure 9a is caused by the mesh-out of the output gear, and the instantaneous state of the gear system at this moment is illustrated in Figure 12. In the figure, the blue arrows represent the normal contact forces, while the red arrows denote the friction forces. At this instant, the mesh between the input gear and the idler gear is in double-tooth contact, whereas the mesh between the output gear and the idler gear is in single-tooth contact.

FIGURE 12

[image: Diagram of two interlocking gears, one large and one small, with colored outlines indicating gear teeth profiles. Red and blue lines show radii and tangents at contact points, demonstrating gear engagement and angular relationships.]

Instantaneous state of the output gear at mesh-out.

The abrupt change in vibration acceleration occurring at 0.01973 s in Figure 9a is caused by the mesh-in of the output gear, and the instantaneous state of the gear train at this moment is illustrated in Figure 13. In the figure, the blue arrows represent the normal contact forces, while the red arrows denote the friction forces. At this instant, both the mesh between the input gear and the idler gear and the mesh between the output gear and the idler gear are in double-tooth contact.

FIGURE 13

[image: Technical illustration displaying two small green-colored gears on the left and right, each engaging with a larger central orange gear with detailed teeth. Red and blue lines indicate axes or force vectors at each contact point, over a grid background.]

Instantaneous state of the output gear at mesh-in.

To validate the accuracy of the proposed model, the gear train parameters specified in Table 2.1 of the Ref ( Martisauskas, 2005). were adopted as the research object. As illustrated in Figure 14, the Root Mean Square (RMS) values of the vibration acceleration at the 3rd harmonic component were calculated under meshing frequencies of 1,200 Hz, 1,600 Hz, and 2000 Hz, which correspond to input rotational speeds of 1895 rpm, 2,526 rpm, and 3,158 rpm, respectively.

FIGURE 14

[image: Line graph showing acceleration a_x in meters per second squared on the y-axis versus frequency f in hertz on the x-axis. The plot forms a triangle, peaking at 57.5184 at 1600 Hz, with 52.1078 at 1200 Hz and 51.3593 at 2000 Hz.]

RMS of the idler vibration acceleration at the 3rd harmonic.

The computational results obtained from Figure 14 were compared with the experimental data presented in Figure 4.73 of the literature. Under the applied load torque of 73.5 N∙m, the results exhibit a distinct non-linear growth trend. Specifically, the values are 52.1078 m/s 2 at 1,200 Hz, 57.5184 m/s 2 at 1,600 Hz, and 51.3593 m/s 2 at 2000 Hz. Although discrepancies exist between the model predictions and the experimental data due to machining errors and assembly tolerances inherent in the test components, both datasets demonstrate a consistent trend, achieving their maximum values around 1,600 Hz. This agreement in tendency validates the accuracy of the proposed model.

### 4.2 Dynamic response of two-gear and three-gear systems under different load torques

When the input rotational speed is 1,000 rpm, the dynamic responses of two-gear and three-gear systems under load torques of 5 N∙m and 100 N∙m are investigated. As shown in Figures 15, 16, the dynamic response of the output gear in the two-gear system under different load torques is illustrated.

FIGURE 15

[image: Panel (a) shows an orange line graph of acceleration in meters per second squared versus time in seconds, with annotations highlighting mesh in and mesh out points and corresponding time intervals. Panel (b) presents a blue line graph of acceleration versus frequency in thousands of Hertz, exhibiting distinct labeled peaks at multiples of the fundamental frequency f_m1.]

The dynamic response of the output gear in the two-gear system under a load torque of 5 N∙m: **(a)**time domain, **(b)**frequency domain.

FIGURE 16

[image: Panel (a) shows a time-domain plot of acceleration in meters per second squared versus time in seconds, with periodic oscillations and annotated mesh in and mesh out points marked by black dots. Panel (b) presents a frequency-domain plot of acceleration versus frequency in thousands of hertz, displaying multiple labeled peaks at harmonics of fundamental frequency f_m1.]

The dynamic response of the output gear in the two-gear system under a load torque of 100 N∙m: **(a)**time domain, **(b)**frequency domain.

In Figures 15a, 16a, when the input rotational speed is consistent, the vibration acceleration variation period under different load torques remains identical at 0.002 s, and the time interval between meshing-out and meshing-in is also consistent at 0.00045 s. The peak-to-peak vibration acceleration is 3 m/s 2 under a load torque of 5 N∙m, and increases to 78 m/s 2 under 100 N∙m. The load torque primarily affects the peak-to-peak vibration acceleration of the output gear, with higher load torques resulting in larger peak-to-peak values. In Figures 15b, 16b, the frequency components of vibration acceleration are dominated by the meshing frequency and its harmonics, with vibration energy concentrated primarily between f m1 and 3f m1.

When the input rotational speed is 1,000 rpm, the dynamic response of the output gear in the three-gear system under different load torques is shown in Figures 17, 18.

FIGURE 17

[image: Panel a shows an orange acceleration waveform versus time with annotated points indicating mesh entry and exit, labeled coordinates, and intervals. Panel b is a line graph displaying acceleration against frequency, with labeled peaks at integer multiples of fm1 from one to ten.]

The dynamic response of the output gear in the three-gear system under a load torque of 5 N∙m: **(a)**time domain, **(b)**frequency domain.

FIGURE 18

[image: Panel (a) shows an orange time-series line graph of acceleration versus time, annotated with mesh in and mesh out points and a labeled period T=0.002 seconds. Panel (b) shows a blue frequency spectrum graph of acceleration versus frequency, with peaks at integer multiples of the fundamental frequency labeled as fm1, 2fm1, 3fm1, and so on up to 10fm1.]

The dynamic response of the output gear in the three-gear system under a load torque of 100 N∙m: **(a)**time domain, **(b)**frequency domain.

In Figures 17a, 18a, the vibration acceleration variation period of the output gear in the three-gear system is 0.002 s, with the time interval between meshing-out and meshing-in being 0.00034 s. The peak-to-peak vibration acceleration is 4 m/s 2 under a load torque of 5 N∙m, and increases to 81 m/s 2 under 100 N∙m. Higher load torques result in larger peak-to-peak vibration acceleration values. In Figures 17b, 18b, the frequency components of vibration acceleration under different load torques are dominated by the meshing frequency and its harmonics, and the vibration energy concentration remains consistent within the same frequency range.

As shown in Figures 19, 20, the dynamic response of the idler gear in the three-gear system under different load torques is illustrated.

FIGURE 19

[image: Panel (a) shows an orange time series plot of acceleration versus time with annotated mesh in and mesh out points, labeled coordinates, and specific time intervals marked. Panel (b) displays a blue frequency spectrum of acceleration versus frequency, highlighting harmonic peaks at integer multiples of the base frequency fm1, from fm1 to 10fm1.]

The dynamic response of the idler gear in the three-gear system under a load torque of 5 N∙m: **(a)**time domain, **(b)**frequency domain.

FIGURE 20

[image: Panel (a) shows a time-domain plot of acceleration versus time, with annotated points marking mesh in and out events and corresponding time intervals. Panel (b) presents a frequency spectrum of acceleration, displaying distinct peaks at integer multiples of a fundamental frequency, each labeled with its multiple.]

The dynamic response of the idler gear in the three-gear system under a load torque of 100 N∙m: **(a)**time domain, **(b)**frequency domain.

In Figures 19a, 20a, the vibration acceleration variation period of the idler gear under different load torques remains consistent, determined by the input rotational speed. However, as the load torque increases, the peak-to-peak vibration acceleration values grow. The peak-to-peak vibration acceleration is 31 m/s 2 under a load torque of 5 N∙m, and increases to 626 m/s 2 under 100 N∙m. Due to the dual interactions with the input gear and the output gear, transient accelerations occur more frequently. In Figures 19b, 20b, the vibration acceleration frequency components under different load torques are dominated by the meshing frequency and its harmonics, with vibration energy concentrated primarily around 8f m1.

### 4.3 Dynamic response of the three-gear system under different installation angles and idler gear teeth numbers

To investigate the influence of installation angles on the dynamic response of the three-gear system, and in Figure 1 were set to different values to establish gear systems with varying installation angles. Table 5 lists the specific values of the installation angles.

TABLE 5

Case | Installation angle | Value |

Case 1 |  | 0° |

 | 0° |

Case 2 |  | 5° |

 | −5° |

Case 3 |  | 10° |

 | −10° |

The specific values of the installation angles.

Figure 21 illustrates the dynamic response of the idler gear in the three-gear system under different installation angles, with an input speed of 1,000 rpm and a load torque of 100 N∙m.

FIGURE 21

[image: Four-panel figure showing acceleration data as time-series plots at left (a, c) and corresponding frequency spectra at right (b, d). Panels (a) and (c) show orange acceleration curves with annotated mesh in/out points and period values. Panels (b) and (d) display blue frequency spectra with labeled harmonic peaks from f_m1 to 10f_m1.]

Vibration acceleration of the idler gear in the *x*-direction under different installation angles in the three-gear system: **(a,b)**Case 2, **(c,d)**Case 3.

In Figures 21a,c, the variation periods of the *x*-direction vibration acceleration for Case 2 and Case 3 remain 0.002 s, with two distinct peaks still present within each cycle. This is consistent with the acceleration characteristics of Case 1 shown in Figure 20. However, the peak values differ: the peak for Case 2 is approximately 637 m/s 2, while that for Case 3 is about 822 m/s 2. As the installation angle increases, the vibration acceleration of the idler gear in the *x*-direction escalates. Figure 21b and (d) illustrate that the dominant frequency of the idler gear’s *x*-direction vibration acceleration consists of the combination frequency and its harmonics. In Figure 20b, the harmonic order corresponding to the maximum amplitude of the acceleration for Case 2 is the 8 th, whereas for Case 3 it is the 6 th. Notably, the harmonic order corresponding to the maximum amplitude decreases as the installation angle increases.

Figure 22 illustrates the dynamic response of the idler gear in the three-gear system under different tooth numbers, with an input speed of 1,000 rpm and a load torque of 100 N∙m.

FIGURE 22

[image: Figure with four panels displaying acceleration data. Panels (a) and (c) show time-domain acceleration a_t versus time t in seconds, with annotated mesh in and mesh out points and labeled period T=0.002 seconds. Panels (b) and (d) show corresponding frequency spectra with acceleration a_t versus frequency f in kilohertz, displaying harmonic peaks labeled with multiples of fundamental frequency f_m1. Upper plots (a, b) display higher acceleration magnitude than lower plots (c, d).]

*X*-direction vibration acceleration of the idler gear in the three-gear system under different tooth numbers: **(a,b)**40 teeth, **(c,d)**80 teeth.

In Figures 22a,c, the variation period of the *x*-direction vibration acceleration for idler gears with 40 and 80 teeth remains 0.002 s, indicating that the meshing period is determined by the rotational speed and tooth number of the input gear, rather than the tooth number of the idler. The peak-to-peak value of the *x*-direction vibration acceleration is 1,505 m/s 2 for the 40-tooth idler, 637 m/s 2 for the 60-tooth idler as shown in Figure 20, and 338 m/s 2 for the 80-tooth idler. These results suggest that the number of idler teeth should be selected to be as close as possible to that of the large gear to minimize the dynamic response. Furthermore, in Figures 22b,d, the harmonic order corresponding to the maximum amplitude of the *x*-direction vibration acceleration is the 8 th for both the 40-tooth and 60-tooth idler gears, while it is the 4 th for the 80-tooth idler. The harmonic order decreases with the increase in tooth number.

## 5 Conclusion

This paper investigates the influence of idler gears on the vibration characteristics of gear systems by constructing a contact dynamics model of a three-gear system. The effects of different input rotational speeds and load torques on the dynamic responses of two-gear and three-gear systems are analyzed. The main conclusions are as follows:

-

Compared to the direct meshing between the input gear and the output gear in a two-gear system, the peak-to-peak vibration acceleration values in the two-gear system are smaller than those in the three-gear system with an idler. The vibration acceleration transients in the output gear of the three-gear system occur more frequently due to the influence of both the input gear and the output gear.

-

The vibration acceleration of the idler gear undergoes four distinct sudden changes within one cycle: meshing-out and meshing-in between the input gear and the idler, and meshing-out and meshing-in between the idler and the output gear. A larger installation angle and a smaller tooth number of the idler gear lead to greater vibration acceleration.

-

Load torque alters the overall peak-to-peak acceleration magnitude of the gear system, higher load torques result in larger peak-to-peak values. However, it has minimal impact on the frequency components and energy distribution of the acceleration.

## Statements

### Data availability statement

The raw data supporting the conclusions of this article will be made available by the authors, without undue reservation.

### Author contributions

ZY: Writing – original draft. YL: Writing – review and editing. LX: Writing – review and editing.

### Funding

The author(s) declared that financial support was received for this work and/or its publication. This research received financial support from the Aeronautical Science Foundation of China (Grant No. 202300020Q9009).

### Conflict of interest

The author(s) declared that this work was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest.

### Generative AI statement

The author(s) declared that generative AI was not used in the creation of this manuscript.

Any alternative text (alt text) provided alongside figures in this article has been generated by Frontiers with the support of artificial intelligence and reasonable efforts have been made to ensure accuracy, including review by the authors wherever possible. If you identify any issues, please contact us.

### Publisher’s note

All claims expressed in this article are solely those of the authors and do not necessarily represent those of their affiliated organizations, or those of the publisher, the editors and the reviewers. Any product that may be evaluated in this article, or claim that may be made by its manufacturer, is not guaranteed or endorsed by the publisher.

### Supplementary material

The Supplementary Material for this article can be found online at: https://www.frontiersin.org/articles/10.3389/fmech.2026.1721474/full#supplementary-material

## References

-

1

Abousleiman V. Velex P. ( 2006). A hybrid 3D finite element/lumped parameter model for quasi-static and dynamic analyses of planetary/epicyclic gear sets. *Mech. Mach. Theory*41 ( 6), 725 – 748. 10.1016/j.mechmachtheory.2005.09.005

  - [CrossRef][4]
  - [Google Scholar][5]
  - View reference in article

-

2

Arian G. Taghvaei S. ( 2021). Dynamic analysis and chaos control of spur gear transmission system with idler. *Eur. J. Mech. - A/Solids*87, 104229. 10.1016/j.euromechsol.2021.104229

  - [CrossRef][6]
  - [Google Scholar][7]

-

3

Autiero M. Paoli G. Cirelli M. Valentini P. P. ( 2024). The effect of different profile modifications on the static and dynamic transmission error of spur gears. *Mech. Mach. Theory*201, 105752. 10.1016/j.mechmachtheory.2024.105752

  - [CrossRef][8]
  - [Google Scholar][9]
  - View reference in article

-

4

Ding H. Rong S. Rong K. Tang J. ( 2022). Semi-FEM dynamic meshing impact forecasting model for spiral bevel and hypoid gear transmission. *Appl. Math. Model.*104, 279 – 305. 10.1016/j.apm.2021.11.014

  - [CrossRef][10]
  - [Google Scholar][11]
  - View reference in article

-

5

Ding X. Y. Kong A. J. Zhang J. T. Chen X. ( 2024). Comprehensive analysis and development of electric-drive-wheel with idler gear. *Actuators*13 ( 9), 336. 10.3390/act13090336

  - [CrossRef][12]
  - [Google Scholar][13]

-

6

Ericson T. M. Parker R. G. ( 2013). Planetary gear modal vibration experiments and correlation against lumped-parameter and finite element models. *J. Sound Vib.*332 ( 9), 2350 – 2375. 10.1016/j.jsv.2012.11.004

  - [CrossRef][14]
  - [Google Scholar][15]
  - View reference in article

-

7

Eritenel T. Parker R. G. ( 2012). An investigation of tooth mesh nonlinearity and partial contact loss in gear pairs using a lumped-parameter model. *Mech. Mach. Theory*56, 28 – 51. 10.1016/j.mechmachtheory.2012.05.002

  - [CrossRef][16]
  - [Google Scholar][17]
  - View reference in article

-

8

Fakhfakh H. Bruyère J. Velex P. Becquerelle S. ( 2015). Simulation of the dynamic behavior of multi-stage geared systems with tooth shape deviations and external excitations. *Multiphysics Model. Simul. Syst. Des. Monit.*, 369 – 378. 10.1007/978-3-319-14532-7_38

  - [CrossRef][18]
  - [Google Scholar][19]
  - View reference in article

-

9

Houser R. Sorenson J. Harianto J. Wijaya H. Satyanarayana M. ( 2002). Comparison of analytical predictions with dynamic noise and vibration measurements for a simple idler gearbox. VDI Ber. 1665, 995 – 1002.

  - [Google Scholar][20]
  - View reference in article

-

10

Hu Y. Tong Z. Tong S. Yang X. ( 2025). Investigating the dynamic behavior of marine gear transmission system considering ship rolling motion. *Int. J. Mech. Sci.*290, 110126. 10.1016/j.ijmecsci.2025.110126

  - [CrossRef][21]
  - [Google Scholar][22]
  - View reference in article

-

11

Kong X. Tang J. Hu Z. Ding H. Wang Z. Wang Q. ( 2023). Dynamic modeling and vibration analysis of spur gear system considering thin-walled gear and hollow shaft. *Mech. Mach. Theory*181, 105197. 10.1016/j.mechmachtheory.2022.105197

  - [CrossRef][23]
  - [Google Scholar][24]
  - View reference in article

-

12

Li D. L. Wang X. Z. ( 2011). “ Ieee. Design for a kind of combined mechanisms based on gear pairs,” in 2011 6th IEEE conference on industrial electronics and applications (ICIEA), 1646 – 1648.

  - [Google Scholar][25]

-

13

Li W. Li Z. Shi H. Li X. ( 2023a). Impact of phase configuration of a helical idler gear system on the vibration. *Appl. Acoust.*211, 109467. 10.1016/j.apacoust.2023.109467

  - [CrossRef][26]
  - [Google Scholar][27]

-

14

Li W. Shi H. Z. Li Z. Y. Hao L. ( 2023b). Analysis of the bending fatigue failure of helical idler gear system considering different fault positions. *J. Of Fail. Analysis And Prev.*23 ( 5), 1940 – 1957. 10.1007/s11668-023-01731-7

  - [CrossRef][28]
  - [Google Scholar][29]
  - View reference in article

-

15

Li W. Li X. F. Li Z. Y. ( 2024). “ Influence of idler misalignment fault on contact and dynamic characteristics of helical gear,” in Proceedings of The Institution of Mechanical Engineers Part K-Journal of Multi-Body Dynamics, 122 – 133. 10.1177/14644193231220523.2381

  - [CrossRef][30]
  - [Google Scholar][31]
  - View reference in article

-

16

Liu G. Parker R. G. ( 2008). Nonlinear dynamics of idler gear systems. *Nonlinear Dyn.*53 ( 4), 345 – 367. 10.1007/s11071-007-9317-z

  - [CrossRef][32]
  - [Google Scholar][33]
  - View reference in article

-

17

Luo Y. Xu L. ( 2025). Contact dynamic modeling and corner contact analysis of the spur gear pair with pitch deviations. *Mech. Syst. Signal Process.*227, 112377. 10.1016/j.ymssp.2025.112377

  - [CrossRef][34]
  - [Google Scholar][35]
  - View reference in article

-

18

Martisauskas S. J. ( 2008). *Experimental study of multi-mesh gear dynamics*. Master’s thesis, Ohio State University. OhioLINK Electronic Theses and Dissertations Center. Available online at: [http://rave.ohiolink.edu/etdc/view?acc_num=osu1731579091203129][36].

  - [Google Scholar][37]
  - View reference in article

-

19

Portron S. Marques P. M. T. ( 2025). A model to study the effect of micropitting on the dynamic behaviour of a geared system. *Mech. Mach. Theory*205, 105854. 10.1016/j.mechmachtheory.2024.105854

  - [CrossRef][38]
  - [Google Scholar][39]
  - View reference in article

-

20

Ramamurti V. Vijayendra N. H. Sujatha C. ( 1998). Static and dynamic analysis of spur and bevel gears using FEM. *Mech. Mach. Theory*33 ( 8), 1177 – 1193. 10.1016/s0094-114x(97)00112-2

  - [CrossRef][40]
  - [Google Scholar][41]
  - View reference in article

-

21

Rook T. E. Singh R. ( 1995). Dynamic analysis of a reverse-idler gear pair with concurrent clearances. *J. Sound Vib.*182 ( 2), 303 – 322. 10.1006/jsvi.1994.0198

  - [CrossRef][42]
  - [Google Scholar][43]
  - View reference in article

-

22

Samani F. S. Molaie M. Pellicano F. ( 2019). Nonlinear vibration of the spiral bevel gear with a novel tooth surface modification method. *Meccanica*54 ( 7), 1071 – 1081. 10.1007/s11012-019-00973-w

  - [CrossRef][44]
  - [Google Scholar][45]
  - View reference in article

-

23

Schlegel R. G. Mard K. C. ( 1967). Transmission noise control-approaches in helicopter design. *Mech. Eng.*, 89 ( 8), 55.

  - [Google Scholar][46]
  - View reference in article

-

24

Singh A. Kahraman A. Ligata H. ( 2008). *Internal Gear Strains and Load Sharing in Planetary Transmissions: Model and Experiments*.

  - [Google Scholar][47]
  - View reference in article

-

25

Tamarozzi T. Ziegler P. Eberhard P. Desmet W. ( 2013). On the applicability of static modes switching in gear contact applications. *Multibody Syst. Dyn.*30 ( 2), 209 – 219. 10.1007/s11044-013-9351-1

  - [CrossRef][48]
  - [Google Scholar][49]

-

26

Thunuguntla S. G. Hood A. A. Cooley C. G. ( 2025). Tooth mesh characterization of spur gears with tooth root crack and surface pit damage. *Eng. Fail. Anal.*169, 109151. 10.1016/j.engfailanal.2024.109151

  - [CrossRef][50]
  - [Google Scholar][51]

-

27

Toda A. Botman M. ( 1979). “ Planet indexing in planetary gears for minimum vibration,” in Design Engineering Technical Conference, St. Louis, Mo ( American Society of Mechanical Engineers), 1979.

  - [Google Scholar][52]
  - View reference in article

-

28

Wang C. Parker R. G. ( 2022). Nonlinear dynamics of lumped-parameter planetary gears with general mesh phasing. *J. Sound Vib.*523, 116682. 10.1016/j.jsv.2021.116682

  - [CrossRef][53]
  - [Google Scholar][54]
  - View reference in article

-

29

Xu L. J. Chen N. ( 2011). Natural properties analysis of an idler gear system of a new NC power Turret. *Adv. Mech. Des. PTS*1 ( 2), 377 – 380. 10.4028/www.scientific.net/amr.199-200.377

  - [CrossRef][55]
  - [Google Scholar][56]
  - View reference in article

-

30

Xu L. Luo Y. Hu R. ( 2024). A novel method of modelling contact dynamics for spur gear transmission. *Mech. Mach. Theory*203, 105793. 10.1016/j.mechmachtheory.2024.105793

  - [CrossRef][57]
  - [Google Scholar][58]
  - View reference in article

-

31

Yu Z. Xu X. ( 2006). Failure analysis of an idler gear of diesel engine gearbox. *Eng. Fail. Anal.*13 ( 7), 1092 – 1100. 10.1016/j.engfailanal.2005.07.015

  - [CrossRef][59]
  - [Google Scholar][60]
  - View reference in article

-

32

Yuan B. Wang J. Han B. Xiong X. Dong H. ( 2025). A novel mathematical model to capture the 3D dynamic contact state of gear pairs considering system flexibility. *Mech. Mach. Theory*209, 105999. 10.1016/j.mechmachtheory.2025.105999

  - [CrossRef][61]
  - [Google Scholar][62]
  - View reference in article

-

33

Zhang X. Dong Y. Wei X. Wang R. Zhang Q. ( 2025). Elastohydrodynamic lubrication performance of curvilinear cylindrical gears based on finite element method. *CMES - Comput. Model. Eng. Sci.*142 ( 2), 1585 – 1609. 10.32604/cmes.2025.059580

  - [CrossRef][63]
  - [Google Scholar][64]
  - View reference in article

-

34

Zhang T. Lin T. Fu L. ( 2025). Analytical and experimental study on acoustic-vibration characteristics of double-helical planetary gear transmission systems with multi-field coupling effect. *Mech. Syst. Signal Process.*224, 112143. 10.1016/j.ymssp.2024.112143

  - [CrossRef][65]
  - [Google Scholar][66]
  - View reference in article

## Summary

Keywords

contact dynamics, idler gear, three-gear system, tooth profile mathematical model, vibration characteristics

Citation

You Z, Luo Y and Xu L (2026) Contact dynamics modeling of a three-gear system and vibration characteristics analysis of the idler gear. *Front. Mech. Eng.*12:1721474. doi: [10.3389/fmech.2026.1721474][67]

Received

09 October 2025

Revised

30 June 2026

Accepted

13 July 2026

Published

31 July 2026

Volume

12 - 2026

Edited by

[Mohamed Ichchou][68], Ecole Centrale de Lyon, France

Reviewed by

[Francesco Pellicano][69], University of Modena and Reggio Emilia, Italy

[Haoran Zou][70], Anhui University of Science and Technology, China

Updates

[image: Crossmark icon]

Check for updates

Copyright

© 2026 You, Luo and Xu.

This is an open-access article distributed under the terms of the [Creative Commons Attribution License (CC BY)][71]. The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.

*****Correspondence: Zhiwei You, [youzhiwei1990@163.com][72]

Disclaimer

All claims expressed in this article are solely those of the authors and do not necessarily represent those of their affiliated organizations, or those of the publisher, the editors and the reviewers. Any product that may be evaluated in this article or claim that may be made by its manufacturer is not guaranteed or endorsed by the publisher.

## Outline

## Figures

## Cite article

Copy to clipboard

Copy citation

Export citation file

- [BibTex][73]
- [EndNote][74]
- [Reference Manager][75]
- [Simple Text file][76]

## Share article

- [77] [Facebook][77]
- [78] [X][78]
- [79] [LinkedIn][79]
- [80] [Email][80]
- WeChat

Share on WeChat

Scan with WeChat to share this article

## Article metrics


## Links

[1]: https://doi.org/10.3389/fmech.2026.1721474
[2]: https://loop.frontiersin.org/people/3235134
[3]: https://loop.frontiersin.org/people/3235116
[4]: https://doi.org/10.1016/j.mechmachtheory.2005.09.005
[5]: http://scholar.google.com/scholar_lookup?author=V..%2BAbousleiman&amp;author=P..%2BVelex&amp;publication_year=2006&amp;title=A%2Bhybrid%2B3D%2Bfinite%2Belement%2Flumped%2Bparameter%2Bmodel%2Bfor%2Bquasi-static%2Band%2Bdynamic%2Banalyses%2Bof%2Bplanetary%2Fepicyclic%2Bgear%2Bsets&amp;journal=Mech.+Mach.+Theory&amp;volume=41&amp;pages=725-748
[6]: https://doi.org/10.1016/j.euromechsol.2021.104229
[7]: http://scholar.google.com/scholar_lookup?author=G..%2BArian&amp;author=S..%2BTaghvaei&amp;publication_year=2021&amp;title=Dynamic%2Banalysis%2Band%2Bchaos%2Bcontrol%2Bof%2Bspur%2Bgear%2Btransmission%2Bsystem%2Bwith%2Bidler&amp;journal=Eur.+J.+Mech.+-+A%2FSolids&amp;volume=87
[8]: https://doi.org/10.1016/j.mechmachtheory.2024.105752
[9]: http://scholar.google.com/scholar_lookup?author=M..%2BAutiero&amp;author=G..%2BPaoli&amp;author=M..%2BCirelli&amp;author=P.%2BP..%2BValentini&amp;publication_year=2024&amp;title=The%2Beffect%2Bof%2Bdifferent%2Bprofile%2Bmodifications%2Bon%2Bthe%2Bstatic%2Band%2Bdynamic%2Btransmission%2Berror%2Bof%2Bspur%2Bgears&amp;journal=Mech.+Mach.+Theory&amp;volume=201
[10]: https://doi.org/10.1016/j.apm.2021.11.014
[11]: http://scholar.google.com/scholar_lookup?author=H..%2BDing&amp;author=S..%2BRong&amp;author=K..%2BRong&amp;author=J..%2BTang&amp;publication_year=2022&amp;title=Semi-FEM%2Bdynamic%2Bmeshing%2Bimpact%2Bforecasting%2Bmodel%2Bfor%2Bspiral%2Bbevel%2Band%2Bhypoid%2Bgear%2Btransmission&amp;journal=Appl.+Math.+Model.&amp;volume=104&amp;pages=279-305
[12]: https://doi.org/10.3390/act13090336
[13]: http://scholar.google.com/scholar_lookup?author=X.%2BY..%2BDing&amp;author=A.%2BJ..%2BKong&amp;author=J.%2BT..%2BZhang&amp;author=X..%2BChen&amp;publication_year=2024&amp;title=Comprehensive%2Banalysis%2Band%2Bdevelopment%2Bof%2Belectric-drive-wheel%2Bwith%2Bidler%2Bgear&amp;journal=Actuators&amp;volume=13
[14]: https://doi.org/10.1016/j.jsv.2012.11.004
[15]: http://scholar.google.com/scholar_lookup?author=T.%2BM..%2BEricson&amp;author=R.%2BG..%2BParker&amp;publication_year=2013&amp;title=Planetary%2Bgear%2Bmodal%2Bvibration%2Bexperiments%2Band%2Bcorrelation%2Bagainst%2Blumped-parameter%2Band%2Bfinite%2Belement%2Bmodels&amp;journal=J.+Sound+Vib.&amp;volume=332&amp;pages=2350-2375
[16]: https://doi.org/10.1016/j.mechmachtheory.2012.05.002
[17]: http://scholar.google.com/scholar_lookup?author=T..%2BEritenel&amp;author=R.%2BG..%2BParker&amp;publication_year=2012&amp;title=An%2Binvestigation%2Bof%2Btooth%2Bmesh%2Bnonlinearity%2Band%2Bpartial%2Bcontact%2Bloss%2Bin%2Bgear%2Bpairs%2Busing%2Ba%2Blumped-parameter%2Bmodel&amp;journal=Mech.+Mach.+Theory&amp;volume=56&amp;pages=28-51
[18]: https://doi.org/10.1007/978-3-319-14532-7_38
[19]: http://scholar.google.com/scholar_lookup?author=H..%2BFakhfakh&amp;author=J..%2BBruy%C3%A8re&amp;author=P..%2BVelex&amp;author=S..%2BBecquerelle&amp;publication_year=2015&amp;title=Simulation%2Bof%2Bthe%2Bdynamic%2Bbehavior%2Bof%2Bmulti-stage%2Bgeared%2Bsystems%2Bwith%2Btooth%2Bshape%2Bdeviations%2Band%2Bexternal%2Bexcitations&amp;journal=Multiphysics+Model.+Simul.+Syst.+Des.+Monit.&amp;pages=369-378
[20]: http://scholar.google.com/scholar_lookup?author=R..%2BHouser&amp;author=J..%2BSorenson&amp;author=J..%2BHarianto&amp;author=H..%2BWijaya&amp;author=M..%2BSatyanarayana&amp;publication_year=2002&amp;title=Comparison%2Bof%2Banalytical%2Bpredictions%2Bwith%2Bdynamic%2Bnoise%2Band%2Bvibration%2Bmeasurements%2Bfor%2Ba%2Bsimple%2Bidler%2Bgearbox&amp;volume=1665&amp;pages=995-1002
[21]: https://doi.org/10.1016/j.ijmecsci.2025.110126
[22]: http://scholar.google.com/scholar_lookup?author=Y..%2BHu&amp;author=Z..%2BTong&amp;author=S..%2BTong&amp;author=X..%2BYang&amp;publication_year=2025&amp;title=Investigating%2Bthe%2Bdynamic%2Bbehavior%2Bof%2Bmarine%2Bgear%2Btransmission%2Bsystem%2Bconsidering%2Bship%2Brolling%2Bmotion&amp;journal=Int.+J.+Mech.+Sci.&amp;volume=290
[23]: https://doi.org/10.1016/j.mechmachtheory.2022.105197
[24]: http://scholar.google.com/scholar_lookup?author=X..%2BKong&amp;author=J..%2BTang&amp;author=Z..%2BHu&amp;author=H..%2BDing&amp;author=Z..%2BWang&amp;author=Q..%2BWang&amp;publication_year=2023&amp;title=Dynamic%2Bmodeling%2Band%2Bvibration%2Banalysis%2Bof%2Bspur%2Bgear%2Bsystem%2Bconsidering%2Bthin-walled%2Bgear%2Band%2Bhollow%2Bshaft&amp;journal=Mech.+Mach.+Theory&amp;volume=181
[25]: http://scholar.google.com/scholar_lookup?author=D.%2BL..%2BLi&amp;author=X.%2BZ..%2BWang&amp;publication_year=2011&amp;title=Ieee.%2BDesign%2Bfor%2Ba%2Bkind%2Bof%2Bcombined%2Bmechanisms%2Bbased%2Bon%2Bgear%2Bpairs&amp;pages=1646-1648
[26]: https://doi.org/10.1016/j.apacoust.2023.109467
[27]: http://scholar.google.com/scholar_lookup?author=W..%2BLi&amp;author=Z..%2BLi&amp;author=H..%2BShi&amp;author=X..%2BLi&amp;publication_year=2023a&amp;title=Impact%2Bof%2Bphase%2Bconfiguration%2Bof%2Ba%2Bhelical%2Bidler%2Bgear%2Bsystem%2Bon%2Bthe%2Bvibration&amp;journal=Appl.+Acoust.&amp;volume=211
[28]: https://doi.org/10.1007/s11668-023-01731-7
[29]: http://scholar.google.com/scholar_lookup?author=W..%2BLi&amp;author=H.%2BZ..%2BShi&amp;author=Z.%2BY..%2BLi&amp;author=L..%2BHao&amp;publication_year=2023b&amp;title=Analysis%2Bof%2Bthe%2Bbending%2Bfatigue%2Bfailure%2Bof%2Bhelical%2Bidler%2Bgear%2Bsystem%2Bconsidering%2Bdifferent%2Bfault%2Bpositions&amp;journal=J.+Of+Fail.+Analysis+And+Prev.&amp;volume=23&amp;pages=1940-1957
[30]: https://doi.org/10.1177/14644193231220523.2381
[31]: http://scholar.google.com/scholar_lookup?author=W..%2BLi&amp;author=X.%2BF..%2BLi&amp;author=Z.%2BY..%2BLi&amp;publication_year=2024&amp;title=Influence%2Bof%2Bidler%2Bmisalignment%2Bfault%2Bon%2Bcontact%2Band%2Bdynamic%2Bcharacteristics%2Bof%2Bhelical%2Bgear&amp;pages=122-133
[32]: https://doi.org/10.1007/s11071-007-9317-z
[33]: http://scholar.google.com/scholar_lookup?author=G..%2BLiu&amp;author=R.%2BG..%2BParker&amp;publication_year=2008&amp;title=Nonlinear%2Bdynamics%2Bof%2Bidler%2Bgear%2Bsystems&amp;journal=Nonlinear+Dyn.&amp;volume=53&amp;pages=345-367
[34]: https://doi.org/10.1016/j.ymssp.2025.112377
[35]: http://scholar.google.com/scholar_lookup?author=Y..%2BLuo&amp;author=L..%2BXu&amp;publication_year=2025&amp;title=Contact%2Bdynamic%2Bmodeling%2Band%2Bcorner%2Bcontact%2Banalysis%2Bof%2Bthe%2Bspur%2Bgear%2Bpair%2Bwith%2Bpitch%2Bdeviations&amp;journal=Mech.+Syst.+Signal+Process.&amp;volume=227
[36]: http://rave.ohiolink.edu/etdc/view?acc_num=osu1731579091203129
[37]: http://scholar.google.com/scholar_lookup?author=S.%2BJ..%2BMartisauskas&amp;publication_year=2008&amp;journal=Experimental+study+of+multi-mesh+gear+dynamics
[38]: https://doi.org/10.1016/j.mechmachtheory.2024.105854
[39]: http://scholar.google.com/scholar_lookup?author=S..%2BPortron&amp;author=P.%2BM.%2BT..%2BMarques&amp;publication_year=2025&amp;title=A%2Bmodel%2Bto%2Bstudy%2Bthe%2Beffect%2Bof%2Bmicropitting%2Bon%2Bthe%2Bdynamic%2Bbehaviour%2Bof%2Ba%2Bgeared%2Bsystem&amp;journal=Mech.+Mach.+Theory&amp;volume=205
[40]: https://doi.org/10.1016/s0094-114x(97)00112-2
[41]: http://scholar.google.com/scholar_lookup?author=V..%2BRamamurti&amp;author=N.%2BH..%2BVijayendra&amp;author=C..%2BSujatha&amp;publication_year=1998&amp;title=Static%2Band%2Bdynamic%2Banalysis%2Bof%2Bspur%2Band%2Bbevel%2Bgears%2Busing%2BFEM&amp;journal=Mech.+Mach.+Theory&amp;volume=33&amp;pages=1177-1193
[42]: https://doi.org/10.1006/jsvi.1994.0198
[43]: http://scholar.google.com/scholar_lookup?author=T.%2BE..%2BRook&amp;author=R..%2BSingh&amp;publication_year=1995&amp;title=Dynamic%2Banalysis%2Bof%2Ba%2Breverse-idler%2Bgear%2Bpair%2Bwith%2Bconcurrent%2Bclearances&amp;journal=J.+Sound+Vib.&amp;volume=182&amp;pages=303-322
[44]: https://doi.org/10.1007/s11012-019-00973-w
[45]: http://scholar.google.com/scholar_lookup?author=F.%2BS..%2BSamani&amp;author=M..%2BMolaie&amp;author=F..%2BPellicano&amp;publication_year=2019&amp;title=Nonlinear%2Bvibration%2Bof%2Bthe%2Bspiral%2Bbevel%2Bgear%2Bwith%2Ba%2Bnovel%2Btooth%2Bsurface%2Bmodification%2Bmethod&amp;journal=Meccanica&amp;volume=54&amp;pages=1071-1081
[46]: http://scholar.google.com/scholar_lookup?author=R.%2BG..%2BSchlegel&amp;author=K.%2BC..%2BMard&amp;publication_year=1967&amp;title=Transmission%2Bnoise%2Bcontrol-approaches%2Bin%2Bhelicopter%2Bdesign&amp;journal=Mech.+Eng.&amp;volume=89
[47]: http://scholar.google.com/scholar_lookup?author=A..%2BSingh&amp;author=A..%2BKahraman&amp;author=H..%2BLigata&amp;publication_year=2008&amp;journal=Internal+Gear+Strains+and+Load+Sharing+in+Planetary+Transmissions%3A+Model+and+Experiments
[48]: https://doi.org/10.1007/s11044-013-9351-1
[49]: http://scholar.google.com/scholar_lookup?author=T..%2BTamarozzi&amp;author=P..%2BZiegler&amp;author=P..%2BEberhard&amp;author=W..%2BDesmet&amp;publication_year=2013&amp;title=On%2Bthe%2Bapplicability%2Bof%2Bstatic%2Bmodes%2Bswitching%2Bin%2Bgear%2Bcontact%2Bapplications&amp;journal=Multibody+Syst.+Dyn.&amp;volume=30&amp;pages=209-219
[50]: https://doi.org/10.1016/j.engfailanal.2024.109151
[51]: http://scholar.google.com/scholar_lookup?author=S.%2BG..%2BThunuguntla&amp;author=A.%2BA..%2BHood&amp;author=C.%2BG..%2BCooley&amp;publication_year=2025&amp;title=Tooth%2Bmesh%2Bcharacterization%2Bof%2Bspur%2Bgears%2Bwith%2Btooth%2Broot%2Bcrack%2Band%2Bsurface%2Bpit%2Bdamage&amp;journal=Eng.+Fail.+Anal.&amp;volume=169
[52]: http://scholar.google.com/scholar_lookup?author=A..%2BToda&amp;author=M..%2BBotman&amp;publication_year=1979&amp;title=Planet%2Bindexing%2Bin%2Bplanetary%2Bgears%2Bfor%2Bminimum%2Bvibration
[53]: https://doi.org/10.1016/j.jsv.2021.116682
[54]: http://scholar.google.com/scholar_lookup?author=C..%2BWang&amp;author=R.%2BG..%2BParker&amp;publication_year=2022&amp;title=Nonlinear%2Bdynamics%2Bof%2Blumped-parameter%2Bplanetary%2Bgears%2Bwith%2Bgeneral%2Bmesh%2Bphasing&amp;journal=J.+Sound+Vib.&amp;volume=523
[55]: https://doi.org/10.4028/www.scientific.net/amr.199-200.377
[56]: http://scholar.google.com/scholar_lookup?author=L.%2BJ..%2BXu&amp;author=N..%2BChen&amp;publication_year=2011&amp;title=Natural%2Bproperties%2Banalysis%2Bof%2Ban%2Bidler%2Bgear%2Bsystem%2Bof%2Ba%2Bnew%2BNC%2Bpower%2BTurret&amp;journal=Adv.+Mech.+Des.+PTS&amp;volume=1&amp;pages=377-380
[57]: https://doi.org/10.1016/j.mechmachtheory.2024.105793
[58]: http://scholar.google.com/scholar_lookup?author=L..%2BXu&amp;author=Y..%2BLuo&amp;author=R..%2BHu&amp;publication_year=2024&amp;title=A%2Bnovel%2Bmethod%2Bof%2Bmodelling%2Bcontact%2Bdynamics%2Bfor%2Bspur%2Bgear%2Btransmission&amp;journal=Mech.+Mach.+Theory&amp;volume=203
[59]: https://doi.org/10.1016/j.engfailanal.2005.07.015
[60]: http://scholar.google.com/scholar_lookup?author=Z..%2BYu&amp;author=X..%2BXu&amp;publication_year=2006&amp;title=Failure%2Banalysis%2Bof%2Ban%2Bidler%2Bgear%2Bof%2Bdiesel%2Bengine%2Bgearbox&amp;journal=Eng.+Fail.+Anal.&amp;volume=13&amp;pages=1092-1100
[61]: https://doi.org/10.1016/j.mechmachtheory.2025.105999
[62]: http://scholar.google.com/scholar_lookup?author=B..%2BYuan&amp;author=J..%2BWang&amp;author=B..%2BHan&amp;author=X..%2BXiong&amp;author=H..%2BDong&amp;publication_year=2025&amp;title=A%2Bnovel%2Bmathematical%2Bmodel%2Bto%2Bcapture%2Bthe%2B3D%2Bdynamic%2Bcontact%2Bstate%2Bof%2Bgear%2Bpairs%2Bconsidering%2Bsystem%2Bflexibility&amp;journal=Mech.+Mach.+Theory&amp;volume=209
[63]: https://doi.org/10.32604/cmes.2025.059580
[64]: http://scholar.google.com/scholar_lookup?author=X..%2BZhang&amp;author=Y..%2BDong&amp;author=X..%2BWei&amp;author=R..%2BWang&amp;author=Q..%2BZhang&amp;publication_year=2025&amp;title=Elastohydrodynamic%2Blubrication%2Bperformance%2Bof%2Bcurvilinear%2Bcylindrical%2Bgears%2Bbased%2Bon%2Bfinite%2Belement%2Bmethod&amp;journal=CMES+-+Comput.+Model.+Eng.+Sci.&amp;volume=142&amp;pages=1585-1609
[65]: https://doi.org/10.1016/j.ymssp.2024.112143
[66]: http://scholar.google.com/scholar_lookup?author=T..%2BZhang&amp;author=T..%2BLin&amp;author=L..%2BFu&amp;publication_year=2025&amp;title=Analytical%2Band%2Bexperimental%2Bstudy%2Bon%2Bacoustic-vibration%2Bcharacteristics%2Bof%2Bdouble-helical%2Bplanetary%2Bgear%2Btransmission%2Bsystems%2Bwith%2Bmulti-field%2Bcoupling%2Beffect&amp;journal=Mech.+Syst.+Signal+Process.&amp;volume=224
[67]: http://dx.doi.org/10.3389/fmech.2026.1721474
[68]: https://loop.frontiersin.org/people/2426030/overview
[69]: https://loop.frontiersin.org/people/2509145/overview
[70]: https://loop.frontiersin.org/people/3482956/overview
[71]: https://creativecommons.org/licenses/by/4.0/
[72]: mailto:youzhiwei1990@163.com
[73]: https://public-pages-files-2025.frontiersin.org/journals/mechanical-engineering/articles/10.3389/fmech.2026.1721474/bibTex
[74]: https://public-pages-files-2025.frontiersin.org/journals/mechanical-engineering/articles/10.3389/fmech.2026.1721474/endNote
[75]: https://public-pages-files-2025.frontiersin.org/journals/mechanical-engineering/articles/10.3389/fmech.2026.1721474/reference
[76]: https://public-pages-files-2025.frontiersin.org/journals/mechanical-engineering/articles/10.3389/fmech.2026.1721474/text
[77]: https://www.facebook.com/sharer/sharer.php?u=https://www.frontiersin.org/journals/mechanical-engineering/articles/10.3389/fmech.2026.1721474/full
[78]: https://www.twitter.com/share?url=https://www.frontiersin.org/journals/mechanical-engineering/articles/10.3389/fmech.2026.1721474/full
[79]: https://www.linkedin.com/share?url=https://www.frontiersin.org/journals/mechanical-engineering/articles/10.3389/fmech.2026.1721474/full
[80]: mailto:?subject=Interesting science article: Contact dynamics modeling of a three-gear system and vibration characteristics analysis of the idler gear&amp;body=Hi!!%0D%0A%0D%0AI think you might find interesting the article &quot;Contact dynamics modeling of a three-gear system and vibration characteristics analysis of the idler gear&quot;.%0D%0A%0D%0AYou can read more about it here: https://www.frontiersin.org/journals/mechanical-engineering/articles/10.3389/fmech.2026.1721474/full
