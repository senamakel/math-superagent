<!-- source: https://arxiv.org/pdf/1610.08176 | converted from PDF -->

arXiv:1610.08176v1  [astro-ph.CO]  26 Oct 2016
Probing statistical isotropy of cosmological radio sources using SKA

Shamik Ghosh, Pankaj Jain, Gopal Kashyap, Rahul Kothari, Sharvari Nadkarni-Ghosh

Physics Department
I.I.T. Kanpur
Kanpur 208016, India

and

Prabhakar Tiwari

Technion- Israel Institute of Technology, 32000 Haifa, Israel

Abstract: There currently exist many observations which are not consistent with the cosmo-
logical principle. We review these observations with a particular emphasis on those relevant for
Square Kilometre Array (SKA). In particular, several diﬀerent data sets indicate a preferred
direction pointing approximately towards the Virgo cluster. We also observe a hemispherical
anisotropy in the Cosmic Microwave Background Radiation (CMBR) temperature ﬂuctuations.
Although these inconsistencies may be attributed to systematic eﬀects, there remains the possi-
bility that they indicate new physics and various theories have been proposed to explain them.
One possibility, which we discuss in this review, is the generation of perturbation modes during
the early pre-inﬂationary epoch, when the Universe may not obey the cosmological principle.
Better measurements will provide better constraints on these theories. In particular, we propose
measurement of the dipole in number counts, sky brightness, polarized ﬂux and polarization
orientations of radio sources. We also suggest test of alignment of linear polarizations of sources
as a function of their relative separation. Finally we propose measurement of hemispherical
anisotropy or equivalently dipole modulation in radio sources.

Keywords: SKA – Cosmological Principal – Kinematic Dipole – Intrinsic Dipole

1 Introduction

The Big Bang model is based on the cosmological principle which states that the Universe is
isotropic and homogeneous, i.e. there is no preferred direction or position. It is essentially an
assumption and cannot be proven on the basis of the symmetries of the fundamental action.
In particular, it applies only in a statistical sense, after averaging over distances of order 100
Mpc. Furthermore there is a preferred frame of reference, the so called cosmic frame of rest.
The Universe appears isotropic and homogeneous only in this frame. Within the Big Bang
paradigm, the Universe may not be isotropic and homogeneous at very early times. It acquires
this property during inﬂation. It has been explicitly shown that starting from a wide range of
anisotropic but homogeneous Bianchi models, the Universe quickly becomes isotropic during
inﬂation (Wald, 1983). However other models also exist which do not obey this principle. In
this article we review the current status of the tests of the cosmological principle. We also
review some of the theoretical attempts to explain the observed violations of this principle.
Observationally it is easier to test isotropy in contrast to homogeneity because it requires
only angular positions of the sources. A test of homogeneity requires three dimensional mapping
of the Universe. Here we shall primarily be interested in observations which test isotropy.
However we point out that an observed violation of isotropy may arise in a fundamental model
which may be anisotropic or inhomogeneous or both.
Even within the Big Bang model, the Universe is not strictly isotropic and homogeneous. It
obeys this property only in a statistical sense in the cosmic frame of rest. For example, let us

1

consider the matter density ρ(t, x) where t is the cosmic time and x the comoving coordinate.
Its spatial distribution can be expressed as,

ρ(t, x) = ρ0(t) + δρ(t, x) . (1)

Here ρ0(t) is the mean density and δρ the ﬂuctuations, such that

⟨δρ(t, x)⟩ = 0 . (2)

Here the angular brackets represent ensemble average. An estimate of this mean is obtained by
averaging δρ over a suﬃciently large patch of the Universe. We expect this distance scale to be
of order 100 Mpc. At smaller scales the matter density shows considerable clustering and the
cosmological principle does not apply. Statistical isotropy (SI) and homogeneity implies

⟨δρ(t, x)δρ(t, x
′)⟩ = f (|x − x
′|) , (3)

i.e., the two point correlations depend only on the distance between the two points and not on
the direction or the position. If we relax the assumption of isotropy then these correlations can
also depend on the direction of the vector x − x′. If we also allow inhomogeneity, then we can
also get dependence on the mean position (x + x′)/2. As we have mentioned above, statistical
isotropy applies only in the cosmic frame of rest. If we are in motion with respect to this frame
with velocity v, then at leading order in |v|, the matter distribution is expected to show a dipole
distribution peaked in the direction of v.
Within the Big Bang model the CMBR temperature ﬁeld can be decomposed as

T (ˆn) = T0 + T1ˆλ · ˆn + ∆T (ˆn) (4)

where ˆn is a unit vector in the direction of observation, T0 the mean temperature, T1 the ampli-
tude of the CMBR dipole, ˆλ the dipole axis and ∆T the primordial ﬂuctuations in temperature.
Here the dipole contains both the kinematic contribution, arising due to local motion, as well
as the contribution due to primordial ﬂuctuations. Hence ∆T contains only multipoles corre-
sponding to l ≥ 2, i.e., quadrupole and higher. We use the spherical polar coordinates (θ, φ) to
label the direction of observation. As in the case of density ﬂuctuations, we have

⟨∆T (ˆn)⟩ = 0 . (5)

Observationally, T0 ≈ 2.73K, T1/T0 ∼ 10−3 and ∆T /T0 ∼ 10−5. Statistical isotropy implies
that the two point correlation function satisﬁes

⟨∆T (ˆni)∆T (ˆnj)⟩ = C(ˆni · ˆnj) , (6)

i.e., it is a function only of the angle between the two observation points ˆni and ˆnj. It is useful
to expand the temperature ﬂuctuations in terms of the spherical harmonics. We obtain

∆T (ˆn)
T0 = ∑

lm almYlm(ˆn) (7)

where alm are the coeﬃcients of this expansion. These also satisfy ⟨alm⟩ = 0. Furthermore
statistical isotropy implies that
 ⟨alma∗
l′m′⟩iso = Clδll′δm,m′ , (8)

where Cl is the standard CMBR power.
The cosmological principle is supported by the Cosmic Microwave Background Radiation
(CMBR) and galaxy surveys. The observed CMBR temperature T (θ, φ) is found to be isotropic

2

to a very good approximation. As mentioned above, the largest deviation from isotropy arises
due to dipole which is of order 10−3. The dominant dipole contribution arises due to the
velocity of the solar system (vCMB) relative to the cosmic frame of rest. Its magnitude vCMB
and direction (l, b) in galactic coordinates are respectively found to be 369 ± 0.9 Km/s and
(263.99◦ ± 0.14◦, b = 48.26◦ ± 0.03◦) (Kogut et al., 1993; Hinshaw et al., 2009). The number
density and brightness of distant radio galaxies are also observed to be isotropic to a good
approximation. However there are many observations which suggest a potential violation of
the cosmological principle. In particular the local velocity vradio extracted from the observed
dipole in the number density and brightness of radio sources is not found to be in agreement
with vCMB. The direction agrees but the magnitude is found to be approximately three times
larger. We review such observed violations of the cosmological principle in the next section. In
section 3 we shall present a theoretical model which may potentially explain these observations.
In section 4 we shall discuss tests of statistical isotropy at Square Km Array (SKA) and will
conclude in section 5.

2 Observed violations of statistical isotropy

The assumption of statistical isotropy is built into the Inﬂationary Big Bang model, which is
the Standard Model of Cosmology. The predictions of the standard model agree remarkably
well with observations which is a real success for the modern era of precision cosmology. Despite
the success of the theory there are tantalizing evidences which highlight small but persistent
departures from the predictions of the isotropic theory. Such observations are mostly in the large
distance scale observations. In this section we will discuss some of the observed violations in
statistical isotropy found in diﬀerent observations with a particular emphasis on those relevant
for SKA.

2.1 Kinematic Dipole

Before we discuss the major observations of SI violation, it is important to understand that the
Cosmological Principle is valid only in the cosmic frame of rest. The Earth is not at rest with
respect to this frame. It is rotating about the Sun, which in turn is rotating about the centre
of the Milky Way; the Milky Way moves with respect to the Local Group barycenter, which
in turn moves about the large scale structures around it. The combined motion due to these
peculiar velocities ensures that our frame of observation has a relative velocity with respect to
the cosmic frame of rest. This leads to a dipole in the observer frame even if the ﬁeld is isotropic
in the cosmic rest frame. This dipole due to Doppler shift of the CMB photons is called the
kinematic dipole.
We denote the peculiar velocity of our observation frame by v and deﬁne β = v/c. If the
temperature ﬁeld and direction in the cosmic rest frame are identiﬁed as T ′ and ˆn′ and the
unprimed symbols denote the observations in our frame, then

T (ˆn) = T ′(n′)
γ(1 − ˆn · β) , (9)

and
 ˆn = ˆn′ + [(γ − 1)ˆn′ · ˆv + γβ]ˆv
γ(1 + ˆn′ · β) (10)

where γ = √1 − β2. Due to Doppler shifting the intensity distribution of the CMB photons
gets modiﬁed. We measure T (ˆn) and use these relations to obtain the temperature ﬁeld in the
cosmic rest frame along with the peculiar velocity of the observation frame.
The large scale structures also acquire a dipole due to Doppler and aberration eﬀects caused
by our local motion. The ﬂux density of radio sources typically shows a power law dependence

3

on frequency. Furthermore the number density of sources depends on the ﬂux density. Most
large scale structure surveys operate in limited frequency ranges and have a lower limit on the
ﬂux density. Due to Doppler eﬀect, the frequencies in the direction of motion of the frame are
blueshifted and are redshifted in the opposite direction. Due to this eﬀect and the intensity
cuts on the survey, sources will shift in and out of the range of observations. Hence in the
direction of motion more objects are blueshifted into the observation frequencies while in the
other hemisphere more sources are redshifted out of the range. Combining the two eﬀects —
the Doppler shift leads to a small dipole in a limited frequency and intensity range large scale
structure survey (Ellis and Baldwin, 1984; Tiwari et al., 2015).
The motion of the reference frame also leads to the aberration eﬀect. This produces a shift
in the angular position of the source. Thus the apparent positions of an isotropic distribution of
sources get shifted towards the direction of motion of the frame, creating a dipole. This eﬀect is
of the same order as β ∼ 10−3 and is relevant for large scale structure dipole studies. Combined
eﬀect of the Doppler shift and aberration produces the kinematic dipole.

2.2 Observed Dipole in Large Scale Structures

Large scale structures are essentially objects formed by non-linear physics. When observed
on small survey volumes the non-linear physics produces structures that would deviate from
isotropy and homogeneity. Thus the local non-linear components of a survey would produce a
local structure dipole. This is not a violation of SI, because the Cosmological Principle is not
valid on this scale. It is only when a very large survey volume, of length scales greater than a
few hundred Mpc, is considered that the Cosmological Principle is applicable and can be tested
for SI violations. If a dipole component is present over and above the local structure and the
kinematic dipole, then it is of cosmological origin and is called the intrinsic dipole. We are
essentially interested in the intrinsic component in SI violation study.
The most signiﬁcant study of dipoles in the large scale structure has been done with the
NRAO VLA Sky Survey (NVSS) radio catalogue containing 1773484 radio sources (Condon et al.,
1998). The survey’s operating frequency is 1.4 GHz and covers the entire northern hemisphere
above a declination of −40◦ and has a mean redshift ∼ 1. For radio sources, in the cosmic rest
frame, the ﬂux density S follows a power law relation with frequency ν, S ∝ ν−α, with α ≈ 0.75.
The diﬀerential number count of radio sources per unit solid angle per unit ﬂux density follows
the power law: n(θ, ϕ, S) ∝ S−1−x, where the spectral index x is close to unity. Due to the
kinematic eﬀects discussed above, it is clear that both the number counts and sky brightness
would show a dipole. We denote these by Dkin
N and Dkin
S respectively. These kinematic dipoles
are given by D
kin
S = [2 + x(1 + α)]β , D
kin
N = [2 + x(1 + α)]β , (11)

i.e. both are described by the same formula (Ellis and Baldwin, 1984; Tiwari et al., 2015; Singal,
2011). Since the velocity of our observation frame with respect to the cosmic rest frame is already
known from CMB experiments, we can make a prediction for the kinematic dipole.
The earliest attempt to extract the NVSS dipole was made by Blake and Wall (2002), where
they claimed to ﬁnd the dipole amplitude approximately two sigmas larger than the expected
kinematic dipole. The extracted direction, however, showed good agreement with expecta-
tions. This was revisited later by several authors, who found an even larger deviation from the
amplitude of the kinematic dipole. These results are summarised in Table 1.
We note that the result obtained by Gibelyou and Huterer (2012) shows a much larger devi-
ation from others. Rubart and Schwarz (2013) have shown that the dipole amplitude estimator
used by Gibelyou and Huterer is biased. It has a direction bias and as a consequence their
dipole direction estimates are not in agreement with other results. The amplitude obtained
by Blake and Wall is smaller than that obtained by any of the other authors. Our study of
the NVSS dipole (Tiwari et al., 2015) involved studying not just the number count but also

4

Authors D0 (×10−2) v (×103 in km/s) (l, b)
Blake & Wall (2002) 1.05 ± 0.42 0.9 ± 0.3 (245◦, 41◦)
Singal (2012) 1.8 ± 0.3 1.32 ± 0.54 (239◦, 44◦)
Gibelyou and Huterer (2012) 2.7 ± 0.5 1.4 ± 0.3 (214◦, 15◦)
Tiwari et. al. (2015) DN 1.25 ± 0.40 1.00 ± 0.32 (261◦, 37◦)
Tiwari et. al. (2015) DS 1.51 ± 0.57 1.21 ± 0.46 (269◦, 43◦)
Rubart and Schwarz. (2013) 1.8 ± 0.6 1.5 ± 0.5 (239◦, 44◦)

Table 1: NVSS observed dipole amplitude, observation frame peculiar velocity and direction. Col-
lected results (Blake and Wall, 2002; Singal, 2011; Gibelyou and Huterer, 2012; Tiwari et al.,
2015; Rubart and Schwarz, 2013) for the NVSS dipole amplitude and direction with ﬂux densi-
ties > 20 mJy (> 15 mJy for Gibelyou and Huterer). Here D0 is the total observed dipole and
v is the peculiar velocity of the observation frame, calculated from D0.

the sky brightness dipole. Both observables show similar results with amplitudes exceeding the
kinematic dipole predictions by approximately two sigmas. Such excess dipole on such large
distance scales suggests a mild signal of potential violation of SI.
The results discussed above while being intriguing need to be reassessed with other data sets
due to the limitations of the NVSS catalogue. The NVSS is compiled by use of two diﬀerent
array conﬁgurations, one above declination of −10◦ and one below. This results in systematics
in the catalogue. The mean number count becomes a function of declination. Plots of number
count density show a large and signiﬁcant dip below a declination of −15◦ and a small but
linear systematic decrease with increasing right ascension. With a ﬂux cut > 15 mJy, the eﬀect
of these systematics can be suppressed to a level where they are no longer visible to the naked
eye while plotting. While the work done with the NVSS data try to limit the eﬀect of such
systematics, having another deep survey with large sky coverage to test out these results would
be very important before we can be sure of SI violation.
The NVSS also contains information about the polarization of the sources. It provides
Stokes parameters Q and U for these sources. Using them we can test the isotropy of sources
with non-zero polarized ﬂux density P , deﬁned as, P = √Q2 + U 2. The polarized ﬂux density,
for radio sources, follows a power law, P ∝ ν−αP , with αP ≈ 0.75. The diﬀerential number
count per unit solid angle, per total ﬂux density S and polarized ﬂux density P is given as
n(θ, ϕ, P, S) ∝ S−1−xP −1−xP in the cosmic rest frame. The kinematic dipole in the number
count of signiﬁcantly polarized sources and the integrated polarized ﬂux density is given by
Tiwari and Jain (2015a):
 D
kin
NP = [2 + x(1 + α) + xP (1 + αP )]β (12)

D
kin
P = [2 + x(1 + α) + xP (1 + αP )]β (13)

As in the case of Eq. 11, we ﬁnd that these dipoles also turn out to be identical. The extracted
velocities are shown in Table 2. It clearly shows a deviation from the expectations of a kinematic
dipole which may indicate the presence of an intrinsic dipole.

Dipole type D0 (×10−2) v (×103 in km/s) (l, b)
DNP 3.3 ± 0.8 2.38 ± 0.61 (207◦, 37◦)
DP 4.9 ± 1.2 2.87 ± 0.68 (244◦, 20◦)

Table 2: NVSS dipole amplitude, observation frame peculiar velocity and direction for sources
with non-zero polarized ﬂux. Results from Tiwari and Jain (2015a) with a lower limit on total
ﬂux density of 30 mJy and polarized ﬂux density range of 0.1 < P < 100 mJy.

Study of Sloan Digital Sky Survey (SDSS) by Itoh et al. (2010) also revealed some fascinating

5

hints of SI violations. The SDSS 6th Data Release photometric catalogue contains over 200
million sources and covers an area of around 8000 deg2, with photometric data in ﬁve band
passes. While the SDSS has a very high ﬁdelity data with low and well understood systematics,
its sky coverage is small – at about 20% with a mean redshift ∼ 0.3. This makes the catalogue
diﬃcult to use for cosmological purpose. There are also some issues which need to be taken
care of in constructing the sample for analysis. The ﬁrst is to ensure that stars are carefully
and reliably removed from analysis. Putting appropriate magnitude range helps in isolating the
galaxies. Another well known feature of the SDSS catalogue is the presence of local clustering
at large scales. The most well known feature of the SDSS is the Sloan Great Wall, at a redshift
of ∼ 0.08. Such local clustering has to be removed reliably before the intrinsic dipole can
be studied. The expected kinematic dipole amplitude in the SDSS is found to be 1.231 ×
10−3 (Itoh et al., 2010). The authors worked with four galaxy samples with diﬀerent ranges
in brightness and photometric redshift. Of them we only discuss two here. These are those
samples which are deepest, more relevant from a cosmological point of view. The results we
discuss are for the bright deep (BD) and the faint deep (FD) samples. For both, the maximum
photometric redshift is ∼ 0.9. The authors performed a χ2 minimisation with the full covariance
matrix. For the BD sample the authors obtained a dipole amplitude of 0.87
+0.59
−0.57 × 10−2 along
(l = 290◦, b = −10◦) ± 100◦. The FD sample gave a dipole amplitude of (1.21 ± 0.23) × 10−2

along (l = 280◦, b = 75◦) ± 33◦.
The authors found a dipole excess in all but the BD sample. They suggested that possible
contamination in the FD samples from incomplete star-galaxy separation and with incorrectly
removed clustering in the data might’ve caused the large measured dipole in this sample. An-
other reason for diﬀerence between the two samples might be the small sky coverage of the
survey. They hoped that a sky survey with a wider coverage would be able to settle the issue.
Yoon et al. (2014) found a dipole in the Wide-ﬁeld Infrared Survey Explorer-Two Micron
All Sky Survey (WISE-2MASS) catalogues. The WISE catalogue has 757 million sources which
are however uncategorised. The authors use the 2MASS catalogue with joint intensity limits to
select data for analysis. The GAMA D2 data was used to model the redshift distribution for the
WISE catalogue. The selected object ﬁeld is shallow with mean redshift of 0.139 and goes up
to a maximum of 0.4. They follow a method similar to that of Gibelyou and Huterer (2012) to
estimate the dipole. With a 20◦ galactic plane cut, the result they obtained was (5.2±0.2)×10−2

along (l = 308◦ ± 4◦, b = −14◦ ± 2◦), which exceeded the theoretical expectations from local
structure dipole. The theoretical dipole amplitude expected being 2.3 ± 1.2. They did not
consider the eﬀect of the kinematic dipole which has an order of magnitude lesser contribution
and could not be suﬃciently tested with the shallow data.
In the last few years the tests of SI violations with large scale structures have gathered steam.
With deeper data and with greater sky coverage, better constraints can be put on SI violations
and thereby constraining SI violating model parameters and mechanisms. With improvement
in data ﬁdelity and understanding of systematics, we may be able to reduce these errors and
ﬁnd out if truly these SI violations are consistent.

2.3 Virgo Alignment

A very curious feature of SI violations is the alignment of various preferred directions in diﬀerent
data sets. Several observations at wide range of frequencies suggest a preferred direction pointing
roughly towards the Virgo supercluster, which is close to the direction of the observed CMBR
dipole. We have already discussed the possible presence of intrinsic dipole in the number
counts, sky brightness as well as polarized radio ﬂux. Furthermore, the CMB quadrupole, CMB
octopole, radio and optical polarizations from distant sources also indicate a preferred direction
pointing roughly towards Virgo. Next we brieﬂy describe each of these eﬀects.
The distribution of polarization angles of distant radio galaxies indicates a dipole pattern.
Here the observable is β = χ−φ, where χ is the linear polarization angle and φ is the orientation

6

angle of the galaxy. This parameter shows a dipole distribution across the sky. The signiﬁcance
of the eﬀect is found to be 3.5σ after making a cut which eliminates the central peak in the
distribution of the rotation measures (RM) (Jain and Ralston, 1999; Jain and Sarala, 2006).
The preferred direction of the dipole is found to be l = 259o, b = 62o in galactic coordinates.
The CMBR quadrupole and the octopole, i.e. multipoles corresponding to l = 2, 3, also
indicate a preferred direction ((l, b) ∼ (250◦, 60◦)), pointing roughly towards Virgo. Statistical
isotropy would imply that these are independent of one another as well of other multipoles, such
as the dipole. However the preferred axis of both these multipoles points approximately in the
direction of the CMB dipole (de Oliveira-Costa et al., 2004; Ralston and Jain, 2004). This is
rather surprising! Furthermore, it is diﬃcult to explain this alignment in terms of bias or fore-
ground eﬀects (Aluri et al., 2011). The procedure for extraction of the preferred direction has
been developed in (de Oliveira-Costa et al., 2004; Ralston and Jain, 2004; Samal et al., 2008).
There also exist other methods for testing statistical isotropy of CMBR (Hajian et al., 2005;
Copi et al., 2007). One may either maximize the angular momentum dispersion ⟨ δT
T |(ˆn · ˆL)2| δT
T ⟩
(de Oliveira-Costa et al., 2004; Bennett et al., 2011). Alternatively one may calculate the prin-
ciple eigenvector of the power tensor for the two modes (Ralston and Jain, 2004; Samal et al.,
2008, 2009). For l = 2, 3 it has a simple interpretation. Both these multipoles appear to be
planar, i.e., all the hot and cold spots lie roughly in the plane. The direction perpendicular to
this is the preferred axis. In more detail, one ﬁnds that most of the contribution to the octopole
power comes from |m| = 3 coeﬃcients. When maximized over direction the |a3,3|2 and |a3,−3|2

contribute approximately 94% of the total power in the octopole (Bennett et al., 2011). This
unusual planar power distribution in octopole is another CMB anomaly at large length scales.
The optical polarizations from distant quasars show an alignment over very large distance
scales (Hutsemekers, 1998; Jain et al., 2004), i.e. the linear polarizations of diﬀerent sources
are observed to point in the same direction. A very strong alignment eﬀect is seen in the
direction of Virgo as well as in the diametrically opposite direction. The angular dependence of
the two point correlations of these polarizations was studied in Ralston and Jain (2004). This
dependence was not found to be statistically signiﬁcant. However it is interesting that the
correlations were found to maximize along an axis pointing towards Virgo (Ralston and Jain,
2004). Hence we see that a wide range of phenomenon, ranging from radio number densities, sky
brightness, polarized ﬂux, polarization angles, CMBR dipole, quadrupole and octopole as well
as the optical polarizations from quasars indicate a preferred direction pointing approximately
towards Virgo. Below we mention one more eﬀect related to CMBR which also indicates this
direction.

2.4 Dipole Modulation in CMBR

The present era of precision cosmology was ushered in by the precision measurements of the
cosmic microwave background (CMB), so our most important indicators of SI violations have
come from the CMB observations. Of the various departures from SI predictions, the dipole
modulation of the CMB temperature ﬂuctuation ﬁeld is the most important. The original claims
were made by Hansen et al. (2004), reporting a hemispherical power asymmetry in the CMB
temperature observations made by the Wilkinson Microwave Anisotropy Probe (WMAP). The
authors masked the galactic plane in the CMB temperature maps and analysed the binned
angular power spectrum on circular patches of varying sizes, oriented about diﬀerent directions
in the sky. They reported signiﬁcantly diﬀerent Cℓ’s in the northern and southern galactic
hemispheres for the multipole range 2 − 40. The 2 − 4 range was reported to have contribution
from the galactic foreground residuals and the signal being directional along the galactic poles.
The power spectrum estimates in 5−40 range however showed asymmetry levels which could not
be justiﬁed by systematics and noise. The asymmetry in 5 − 40 range was found to maximize
along (57◦, 10◦) in Galactic coordinates, which is close to the ecliptic axis. In the frame of
maximum asymmetry, they found that all the 5 − 40 multipoles in the northern hemisphere

7

have less power than than the average amplitudes, while in the southern hemisphere most of
the multipoles in the range have more power than the average amplitude. The authors also
claimed a similar signal of lower signiﬁcance in the COsmic Background Explorer (COBE) data
thereby ruling out systematics as a possible source of the signal.
Gordon (2007) proposed a model of linear modulation of the isotropic temperature ﬂuc-
tuation ﬁeld to phenomenologically represent hemispherical anisotropy. In this model, the
temperature ﬂuctuation (δT ) observed along a direction ˆn, is given by

δT (ˆn) = δTiso(ˆn) [1 + f (ˆn)] , (14)

where f (ˆn) is a direction dependent function that modulates δTiso, the isotropic temperature
ﬂuctuation ﬁeld1. The modulating function f (ˆn) is assumed as Aˆλ · ˆn. This linear modulation
along a preferred direction ˆλ and with amplitude A, would result in a dipole modulation at
the surface of last scattering. However, it is important to understand that hemispherical power
asymmetry is not the same as dipole modulation. A dipole modulation model will naturally
give rise to hemispherical asymmetry but hemispherical power asymmetry does not necessitate
a dipole modulation.
In 2009, following the release of WMAP ﬁve-year data, Hoftuft et al. (2009) estimated the
three parameters A, and two components of ˆλ from the data, maximizing the log-likelihood for
the dipole modulation model. The observed data along a direction (ˆn) is written as in (14) but
with an additive noise term to read d(ˆn) = δT (ˆn) + N (ˆn). The signal covariance matrix for
such a model is given by (Hoftuft et al., 2009)

Smod(ˆn, ˆm) = [1 + Aˆλ · ˆn
] Siso(ˆn, ˆm) [1 + Aˆλ · ˆm] . (15)

The isotropic signal covariance matrix Siso is written as

Siso(ˆn, ˆm) = 1
4π
 ∑

i (2ℓ + 1)CℓPℓ(ˆn · ˆm) . (16)

Here the Pℓs are the Legendre polynomials. The full covariance matrix then reads (Hoftuft et al.,
2009) C = Smod(A, ˆλ) + Siso + N + F, (17)

with N and F as noise covariance and foregrounds respectively. Assuming the signal and noise
both to be Gaussian the log-likelihood takes the form (Hoftuft et al., 2009):

− 2lnL(A, ˆλ) = dT C−1d + ln|C|. (18)

The best-ﬁt results in the ℓ ≤ 64 range, obtained by maximizing the log-likelihood, are given in
Table 3. The dipole modulation signal was claimed with a 3.3σ signiﬁcance for ℓ ≤ 64.
It has been shown (Prunet et al., 2005; Rath and Jain, 2013) that for a dipole modulated
temperature ﬂuctuation ﬁeld given by Eq. 14, with the preferred direction ˆλ chosen along ˆz,
the two point correlation function of the spherical harmonic coeﬃcients aℓm is given by

⟨aℓma
∗
ℓ′m′⟩ = ⟨aℓma∗
ℓ′m′⟩iso + ⟨aℓma
∗
ℓ′m′⟩dm
= Cℓδℓℓ′δmm′ + A (Cℓ′ + Cℓ) ×
[√ (ℓ − m + 1)(ℓ + m + 1)
(2ℓ + 1)(2ℓ + 3) δℓ′,ℓ+1 +
 √ (ℓ − m)(ℓ + m)
(2ℓ + 1)(2ℓ − 1) δℓ′,ℓ−1
]
 δm′m. (19)

This implies that for a dipole modulated temperature ﬁeld, the covariance matrix, in spherical
harmonic space is not diagonal. The added modulation gives rise to non-zero correlations

1Note that we have changed the sign in front of f (ˆn) from ‘−’ to ‘+’ to keep consistency with later work.

8

Result from A (l,b)
Hoftuft et al. (2009) (W5) 0.072 ± 0.022 (224◦, −27◦) ± 24◦

Ade et al. (2014) (P13) 0.065 ± 0.021 (226◦, −17◦) ± 24◦

Ade et al. (2015) (P15) 0.066 ± 0.021 (225◦, −18◦) ± 24◦

Rath et al. (2015) (W9) 0.090 ± 0.029 (227◦, −14◦)
Rath et al. (2015) (P13) 0.074 ± 0.019 (229◦, −16◦)
Ghosh et al. (2016) (P15) 0.078 ± 0.019 (242◦ ± 16◦, −17◦ ± 20◦)

Table 3: Best-ﬁt values for the dipole modulation parameters. W5 and W9 stand for WMAP
ﬁve-year and nine-year datasets respectively, P13 and P15 stand for Planck 2013 and 2015
SMICA maps.

between ℓ and ℓ ± 1 multipoles. So we have studied the dipole modulation feature using this
property of non-zero ℓ, ℓ + 1 correlations by deﬁning a statistic SH as

SH =
 ℓmax∑

ℓ=ℓmin
 ℓ(ℓ + 1)
(2ℓ + 1)
 ℓ∑

m=−ℓ aℓma∗
ℓ′m′ (20)

which is a summed estimate of the ℓ, ℓ+1 correlations in the range ℓmin ≤ ℓ ≤ ℓmax. The analysis
was performed by setting ℓmin = 2 and ℓmax = 64, 128 for extraction of diﬀerent parameters.
Some of the results of this analysis are shown in Table 3 and show good agreement with other
estimates.
The hemispherical power asymmetry has persisted in the data for three generations of satel-
lite based CMB experiments. The Planck experiment team has tested for both the hemispher-
ical power asymmetry and dipole modulation in their CMB data, ﬁnding evidence for both
(Ade et al., 2014, 2015). The dipole modulation signal has persisted at ∼ 3σ level in the 2013
and 2015 data release. The results of the Planck team and the corresponding results with the
statistic SH are shown in Table 3 for comparison.
A test of dipole modulation or equivalently hemispherical anisotropy for the polarization E
modes has also been carried out in Ghosh et al. (2016). The low l multipoles of the polarization
ﬁeld are unreliable. Hence the authors only considered multipoles l ≥ 40. Furthermore they
did not test the signiﬁcance of the eﬀect since it required extensive numerical work in modelling
detector noise. Interestingly it was found that the preferred direction in the range 40 ≤ l ≤ 100
again points in the direction of Virgo. The direction starts to shift as we extend the upper limit
on l. Although the statistical signiﬁcance of the eﬀect is unknown, it is interesting that the low
l multipoles again prefer a direction towards Virgo.

2.5 Dipole Modulation in large Scale Structures

A signal of the dipole modulation has also been investigated in the large scale structures. The
ﬁrst attempt in this direction was made by Hirata (2009) using SDSS quasars. His approach
to the problem of searching for dipole modulation in the large scale structures was based on
the variation of the amplitude of the linear power spectrum σ8. If the CMB hemispherical
asymmetry and dipole modulation are of cosmological origins then they should be linked to the
primordial curvature perturbations. Such a situation would lead to a gradient in the amplitude
of the power spectrum along the preferred direction of the dipole. Since the growth and abun-
dance of large scale structures is very sensitive to the value of σ8, the gradient of this parameter
can be constrained from the number variations of the large scale structures.
The SDSS quasars were chosen by Hirata to test out the variation of σ8. This set had deep
distance spread with wide angular coverage. Since these are SDSS objects, the systematics are
fairly well understood. One of the drawbacks of the dataset chosen is that the number density
of such quasars is small, roughly 1 deg−2. When the preferred direction is ﬁxed along that

9

obtained by Eriksen et al. (2007) (l = 225◦, b = −27◦), the amplitude of dipole modulation was
found as A = −0.0018 ± 0.0044. A search for the best ﬁt direction did not reveal a statistically
signiﬁcant signal. Overall, Hirata’s work is strongly indicative of no dipole modulation in the
large scale structures.
Fern´andez-Cobos et al. (2014) searched for the dipole modulation signal in the NVSS. Their
approach is a logical extension of the Hoftuft et. al. method, described at the beginning
of this section, to the large scale structures, working with the galaxy angular power spectra
C GG
ℓ . They worked with three lower ﬂux cuts of 2.5, 5.0 and 10.0 mJy. They corrected for the
declination dependent systematics, only for the case of the 2.5 mJy cut, by dividing the entire
data map into 70 strips of equal area and rescaling the number density. From their simulation
they forecasted a non-negligible dipole modulation with A = 0.065 ± 0.013 along the direction
(l = 224◦, −14◦) ± 17◦. However they did not ﬁnd any evidence of dipole modulation in data.
The modulation amplitude A was found to be 0.003 ± 0.015 for 2.5 mJy cut, 0.011 ± 0.016 for
5.0 mJy cut and 0.007 ± 0.014 for 10.0 mJy cut, all of the amplitudes being compatible with
null result.

2.6 Alignment of linear polarizations of radio sources

The linear polarizations of radio sources show alignment with one another, analogous to the
alignment of optical polarizations from quasars. An alignment on the distance scale of 100 Mpc
was reported in Tiwari and Jain (2013) in the JVAS/CLASS sources with polarized ﬂux greater
than 1 mJy. This has subsequently been conﬁrmed (Shurtleﬀ, 2014; Pelgrims and Hutsem´ekers,
2015). An alignment on larger distance scales for the subsample of QSOs in this data set has
also been reported in Pelgrims and Hutsem´ekers (2015). An alignment on the scale of 100 Mpc
may be expected within the framework of Big Bang cosmology since sources show correlation
with one another on such distance scales. In Tiwari and Jain (2015b) the authors argued that
this alignment is induced by the correlations in the supercluster magnetic ﬁeld. Within the
framework of this model the authors extracted the spectral index of the magnetic ﬁeld on
supercluster scales of order 100 Mpc. The extracted value was found to be equal to 2.74 ± 0.04.
Cosmological magneto-hydrodynamic simulations (Dolag et al., 2002) on cluster scales of order
few Mpc lead to a spectral index of 2.70 which is, surprisingly, in good agreement with the value
extracted in Tiwari and Jain (2015b). However this may be merely a coincidence since the two
refer to very diﬀerent distance scales. The eﬀect claimed in Tiwari and Jain (2015b) needs to
be tested carefully by future surveys. The alignment might arise due to bias and furthermore it
is found that the signiﬁcance of the eﬀect reduces considerably if the jackknife errors are taken
into account (Tiwari and Jain, 2015b). The authors argued that we require at least four times
larger data set in order to have a reliable conﬁrmation of this eﬀect.

2.7 Other Anomalies

Other CMB anomalies worth mentioning are the Cold Spot and the parity asymmetry. Cruz et al.
(2005) reported an anomalous cold spot at (l = 209◦, b = −57◦) with a size of 10◦. To under-
stand the parity asymmetry we have to think of the temperature ﬁeld being sum of even and
odd parity ﬁelds. The even and odd parity can be characterised by

P + =
 ℓmax∑

ℓ=2 2
−1(1 + (−1)
ℓ)ℓ(ℓ + 1)/2πCℓ (21)

P − =
 ℓmax∑

ℓ=2 2
−1(1 − (−1)
ℓ)ℓ(ℓ + 1)/2πCℓ (22)

The ratio P +/P − denotes the ratio of the even parity contribution to the odd parity contri-
bution. It was reported around 2010 (Kim and Naselsky, 2010; Aluri and Jain, 2012), that the

10

ratio is anomalously large when summing over the largest angular scales. Summing the multi-
poles 2 ≤ ℓ ≤ 22 the results for the ratio for WMAP 7 year data was 0.71, indicating a larger
contribution from the even parity. Both these anomalies continue to exist in the Planck CMB
data.

3 Theoretical Expectations

It is generally believed that the eﬀects reviewed in the previous section are inconsistent with
the Big Bang cosmological model. Although these observations appear to be in conﬂict with
the cosmological principle, it has been shown in (Aluri and Jain, 2012; Rath et al., 2013) that
they can be accommodated within the Big Bang paradigm. The basic idea is that the early
pre-inﬂationary phase of the Universe may not be isotropic and homogeneous. It acquires
this property during the early phase of inﬂation. This has been explicitly demonstrated for
the case of Bianchi models (Wald, 1983) which are anisotropic but homogeneous. It has also
been shown that, for a wide range of parameters, modes generated during this early period
can re-enter the horizon before the current era and hence aﬀect observations (Aluri and Jain,
2012; Rath et al., 2013). This implies that although the background evolution is isotropic and
homogeneous, the perturbations need not respect the cosmological principle. Interestingly the
dominant eﬀect is expected for low k modes, which observationally appear to show the largest
deviation from isotropy. This phenomenon has been explicitly demonstrated in Rath et al.
(2013) where the quadrupole and octopole alignment is explained in terms of an early anisotropic
phase of inﬂation. Similar ideas have been explored in order to explain the hemispherical
anisotropy (Rath et al., 2015; Jain and Rath, 2015; Kothari et al., 2015a; Ghosh et al., 2016).
However in this case an explicit model requires either an inhomogeneous Universe (Carroll et al.,
2010; Rath et al., 2015) or space-time noncommutativity (Jain and Rath, 2015; Kothari et al.,
2015b). A detailed analysis of such models is so far not available in the literature. Here we
brieﬂy review some basic results which have been obtained by assuming a model of primordial
power spectrum.
Let us ﬁrst consider the primordial power spectrum in real space, deﬁned as,

F (R, X) = ⟨δ(x)δ(x ′)⟩ (23)

where δ(x) is the primordial density ﬂuctuation at comoving coordinate x, R = x − x ′ and
X = (x + x ′)/2. In Kothari et al. (2015a) the authors consider the following inhomogeneous
model:
 F (R, X) = f1(R) + sin (λ · X
τ0 + δ) f2(R), (24)

where ˆλ and δ are parameters and τ0 is the current conformal time. Here the second term
represents the contribution due to inhomogeneity. In Fourier space, the corresponding power
spectrum is given by,

〈δ(k)δ∗(k
′)
〉 = Piso(k)δ3 (
k − k
′) − i
2 g(k+) [δ3 (k − k
′ + λ
τ0
 ) − δ3 (k − k
′ − λ
τ0
 )] (25)

where
 g (k+) = ∫ d3R
(2π)3 exp [i (k + k
′) · R
2
 ] f2(R),

and k+ = (k+k′)/2. This model leads to correlations between multipoles l and l ±1 of CMB, as
expected in the case of dipole modulated temperature ﬁeld (see Eq. 19). Kothari et al. (2015a)
parameterize the function g(k) as a power law, i.e.,

g(k) = g0Piso(k)(kτ0)
−α (26)

11

where g0 and α are parameters. A ﬁt to the CMB dipole modulation data suggests that
α ≈ 1. A similar analysis has also been carried out for an anisotropic but homogeneous model
(Kothari et al., 2015a). As explained earlier, such a model is not possible in commutative
spacetimes. However it may arise within the framework of noncommutative spacetimes.
A study of the implications of such a primordial model on large scale structures is so far
not available in the literature. We expect that predictions based on such models will become
available by the time SKA becomes operational.

3.1 The galaxy power spectrum

For tests at SKA our primary aim is to study the distribution of galaxies at large distances
or equivalently their angular power spectrum Cl. We next brieﬂy discuss the relation between
ΛCDM power spectrum P (k) to Cl. Let N (ˆr) be the projected number density (per steradian)
in the direction ˆr, and ¯N be the mean number density averaged over the sky. We write the
number density N (ˆr) = ¯N (1 + ∆(ˆr)), where ∆(ˆr) represents the projected number surface
density contrast. Let the three-dimensional dark matter density contrast be represented as
δm(r, z(r)), where (r, z(r)) represent a unique location in space and time. The vector r stands
for comoving distance r in direction ˆr and z(r) is the redshift corresponding to comoving distance
r. Assuming linear galaxy biasing b(z) and linear growth factor D(z) of density contrast we
write the corresponding galaxy contrast δg(r, z(r)) = δm(r, z = 0)D(z)b(z). Now we can write
the theoretical expression for ∆(ˆr) as,

∆(ˆr) = ∫ ∞

0 δg(r, z(r))p(r)dr

= ∫ ∞

0 δm(r, z = 0)D(z)b(z)p(r)dr, (27)

where p(r)dr is the probability of observing a galaxy between r and (r + dr). The expansion of
∆(ˆr) in spherical harmonics and subsequent harmonic coeﬃcients, ˜alm, similar to equation (7),
is given as,
 ˜alm = ∫ dΩ∆(ˆr)Ylm(ˆr) (28)

= ∫ dΩYlm(ˆr) ∫ ∞

0 δm(r, z = 0)D(z)b(z)p(r)dr .

To write the harmonic coeﬃcients, ˜alm, in terms of the k-space density ﬁeld δk, we expand
δm(r, z = 0) in Fourier domain,

δm(r, z = 0) = 1
(2π)3
 ∫ d
3kδke
ik·r , (29)

and substitute e
ik·r = 4π ∑

l,m i
ljl(kr)Y ∗
lm(ˆr)Ylm(ˆk) ,

where jl is the spherical Bessel function of ﬁrst kind for integer l. Subsequently we write

˜alm = il

2π2
 ∫ D(z)b(z)p(r)dr ∫ d
3kδkjl(kr)Y ∗
lm(ˆk) . (30)

Following equation (30) we write the theoretical angular power spectrum ˜Cl as,
˜Cl = 〈|˜alm|
2〉

= 2
π
 ∫ dkk2P (k) ∣
∣
∣
∣
∫ ∞

0 D(z)b(z)p(r)drjl(kr)
∣
∣
∣
∣
2

= 2
π
 ∫ dkk2P (k)W 2(k) . (31)

12

where W (k) = ∫ ∞
0 D(z)b(z)p(r)drjl(kr) is the window function in k-space. We have also used
⟨δkδk′⟩ = (2π)3δ(k − k′)P (k) where P (k) is ΛCDM power spectrum.

3.2 Observational Cl

The observational estimate of Cl analogous to theoretical ˜Cl given in equation (31) is,

C obs
l = ⟨|a′
lm|2⟩
Jlm − 1
¯N (32)

where a′
lm = ∫
survey dΩ∆(ˆr)Ylm(ˆr) and Jlm = ∫
survey |Ylm|2dΩ, the Jlm is an approximate correc-

tion factor for the partial survey region (Peebles, 1980). The term 1
¯N removes the contribution
from the Poissonian shot-noise.
The error in above estimate of power spectrum due to cosmic variance, sky coverage and
shot-noise is as follows:
 ∆Cl =
 √ 2
(2l + 1)fsky
 (C obs
l + 1
¯N
 ) (33)

where fsky is the fraction of sky observed in the survey. Notice that the above error estimate
is applicable in case of the 2-point galaxy-galaxy angular power spectrum (C gg
l ). The lensing
shear power spectrum is deduced considering shape measurements of the galaxies. The shear
angular power spectrum error estimate is given by,

∆Cl =
 √ 2
(2l + 1)fsky
 (C obs
l + σ2
ǫ
¯N
 ) (34)

where σǫ is the RMS variance of the ellipticity distribution. Furthermore, for the case of
polarized sources, assuming that the polarization position angle is an unbiased tracer of the
intrinsic morphological orientation of the galaxy with a scatter of αrms, the corresponding error
estimate is as follows (Brown and Battye, 2011b,a):

∆Cl =
 √ 2
(2l + 1)fsky
 (C obs
l + 16α2
rmsσ2
ǫ
¯N
 ) . (35)

4 Tests of statistical isotropy at SKA

We propose the following tests of statistical isotropy in large scale structures:

1. Determination of the dipole in number counts and sky brightness of radio sources in order
to test its consistency with the kinematic dipole.

2. Determination of the dipole in number counts of signiﬁcantly polarized radio sources as
well as in the polarized ﬂux.

3. Testing the alignment of linear polarizations of radio sources as a function of their relative
separation.

4. Testing the presence of dipole modulation in radio sources.

5. Determination of the dipole anisotropy in the oﬀsets between linear polarization angles
and the galaxy orientation angles.
 13

4.1 SKA technical details and capabilities

The SKA will be a highly ﬂexible instrument with unprecedented observational capabilities.
It will consist of an inner core and outer stations arranged in a log-spiral pattern. The full
array will be extended to at least 3000 km from the central core. This will be the largest radio
telescope in the world and will revolutionize our understanding of the Universe. The SKA will
operate in frequency range from 70 MHz to 10 GHz (see Dewdney et al. (2013) for more details).
The SKA will perform both redshift (HI) and radio continuum surveys in the aforementioned
frequency range. There will be two phases of SKA observations. The ﬁnal phase is expected
to map out 1 billion galaxies over a sky area of fsky ∼ 3/4, out to a redshift of z ∼ 2. This
will reduce the shot-noise in galaxy angular power spectrum (see equation (32)) by a factor of
3000. The resulting shot-noise will be 3 orders of magnitude lower than ΛCDM ˜Cl and will be
negligible in comparison to cosmic variance (equation (33)).
The SKA will yield measurements of various cosmological parameters with unmatched pre-
cision. The anisotropy tests at various scales will improve immensely. The dipole anisotropy
observed in NVSS brightness and polarization will be clearly settled. At present the signal is
observed at ∼ 3σ (Tiwari et al., 2015). The radio galaxy biasing consideration gives similar
signiﬁcance for reasonable radial number density and galaxy bias values (Tiwari and Nusser,
2015). The galaxy-bias is a nuisance in relating the galaxy clustering to underlying dark matter
distribution. The biasing is almost stochastic, scale-dependent, redshift dependent and non-
linear (Dekel and Lahav, 1999). The bias determination is almost always indirect as we always
need the underlying dark matter density power spectrum to extract bias from galaxy cluster-
ing. As discussed earlier, the NVSS total source count is ∼ 1.8 × 106. The SKA source count is
expected to be roughly two orders of magnitude larger (Wilman et al., 2008). This also applies
to the polarized source density. The wide and deep polarization surveys with SKA will reach
to µJy ﬂux limit. The deep polarization survey (2 µJy) will probe the source population as
a function of ﬂux, luminosity and redshift, whereas the wide (33,000 deg2, sensitive up to 10
µJy ) survey will reveal the large scale clustering of polarized galaxies. Hence the statistical
error in source counts, sky brightness, polarized number count as well as polarized ﬂux will be
suﬃciently small in order to reliably extract the signal of dipole anisotropy. However one has
to carefully remove systematic eﬀects from data.
Besides the galaxy biasing described above, the most important systematic eﬀect is the con-
tribution due to local clustering dipole (Blake and Wall, 2002; Singal, 2011; Gibelyou and Huterer,
2012; Rubart and Schwarz, 2013; Tiwari et al., 2015; Schwarz et al., 2015). So far this has been
removed by cross correlating with catalogues of known nearby galaxies (Blake and Wall, 2002).
With SKA redshift survey the exact radial number density will be known. The large area sur-
vey coverage and depth in redshift with SKA observation will allow us to measure the galaxy
clustering at the largest scale ever. The SKA galaxy power spectrum will cover the turnover
(k < 0.02 h Mpc−1) of ΛCDM power spectrum. This will also allow a better constrain on
galaxy bias. The NVSS survey also suﬀers from signiﬁcant declination bias due to two diﬀerent
array conﬁgurations used for diﬀerent declinations. While this may not be an issue for SKA, a
declination bias centered at the array location may arise (Tiwari and Jain, 2015a). Such a bias
has been identiﬁed in the NVSS survey, particularly for the sample with low ﬂux cutoﬀ, and
can be eﬀectively removed by the procedure described in (Tiwari and Jain, 2015a). Yet another
systematic eﬀect arises in relating the extracted dipole from data to the local speed. The main
issue here is the deviation of the distribution of number density n(S) as a function of the ﬂux
S from a pure power law. However it has been shown that a generalized distribution ﬁts the
data very well and one can extract the local speed very accurately using this ﬁt (Tiwari et al.,
2015; Tiwari and Jain, 2015a).
Further the resolved shape of billion galaxies from SKA will give the best shear measure-
ments. The light rays from distant galaxies follow the geodesics, which bend according to the
presence of matter in intervening space. This results in a shape distortion following the matter

14

distribution ﬂuctuations along the line of sight. This enables a direct mapping of mass dis-
tribution (luminous + non-luminous) and dark energy measurements. The statistical error in
auto-shear power spectrum with SKA will decrease by a factor of ∼ 3000 due to high number
surface density (∼ 105 deg2) and reliable shape measurements (Demetroullas and Brown, 2016).
With such huge improvement in statistics, it will be challenging to control the corresponding
systematics. Cross-correlations between shear maps from SKA and LSST/Euclid can remove
observational systematics.
The enhanced polarization survey at SKA will also allow us to reliably test the alignment
of linear polarizations as a function of the angular separation among galaxies (Tiwari and Jain,
2013, 2015b). With two orders of magnitude increase in the number of sources, the eﬀect
will be seen clearly if present in data. Furthermore the SKA redshift survey would allow
a 3 dimensional analysis which will provide an unambiguous test of this phenomenon, both
at the supercluster scale (Tiwari and Jain, 2013, 2015b) and on larger cosmological distance
scales (Pelgrims and Hutsem´ekers, 2015). Within the framework of the theoretical model of
Tiwari and Jain (2015b), it will allow a clean extraction of the spectral index of the supercluster
magnetic ﬁeld at distance scales of order 100 Mpc. On cluster scales of order few Mpc, cosmo-
logical magneto-hydrodynamic simulations lead to a spectral index of 2.7 for the corresponding
magnetic ﬁeld. It may be interesting to apply the formalism proposed in Tiwari and Jain
(2015b) and extract the magnetic ﬁeld spectral index by studying correlations between the ra-
dio linear polarizations at this distance scale. This will require large amount of data on linear
polarizations of galaxies separated by distances of order Mpc. Such a measurement may also
be feasible at SKA.
SKA will also make measurements of linear polarizations at diﬀerent frequencies for a very
large sample of sources (Beck and Gaensler, 2004; Haverkorn et al., 2015). The main purpose
of these observations is the determination of Faraday rotation measures which will provide
information about the milky way magnetic ﬁeld. However these will also allow measurements
of the host polarization position angles. For the case of active galaxies, if we are also able
to determine the orientation of the jets, it is possible to test the dipole anisotropy claimed in
Jain and Ralston (1999). We point out that extraction of rotation measures and polarization
position angles may be facilitated by the reﬁned technique developed in Sarala and Jain (2002).

5 Discussion and Conclusions

The tantalizing possibility that the Cosmological principle may be violated is indicated by
many observations. The most prominent of these eﬀects is the so called Virgo Alignment,
which refers to a wide range of phenomena indicating a preferred direction pointing towards
Virgo. The SKA has the capability to convincingly test several of these eﬀects. These include
the dipole anisotropy in radio polarization angles (Jain and Ralston, 1999), the dipole in the
number counts and sky brightness (Blake and Wall, 2002; Singal, 2011; Gibelyou and Huterer,
2012; Tiwari et al., 2015; Rubart and Schwarz, 2013) and in the polarized number counts and
polarized ﬂux (Tiwari and Jain, 2015a). These observations may indicate that we need to
go beyond the standard Big Bang cosmology. Alternatively they may be explained by pre-
inﬂationary anisotropic and/or inhomogeneous modes (Aluri and Jain, 2012; Rath et al., 2013).
In either case, conﬁrmation of this alignment eﬀect is likely to revolutionize cosmology. SKA
will also test the signal of dipole modulation in large scale structure. Finally it will test the
alignment of radio polarizations. It has been suggested that the alignment is induced by the
correlations in the cluster magnetic ﬁeld (Tiwari and Jain, 2015b). Hence, if conﬁrmed, this
phenomenon might provide a tool to study the statistical properties of the large scale magnetic
ﬁeld.
 15

Acknowledgements

Rahul Kothari sincerely acknowledges CSIR, New Delhi for the award of fellowship during the
work.

References

Ade, P. A. R. et al. (2014). Planck 2013 results. XXIII. Isotropy and statistics of the CMB.
Astron. Astrophys., 571:A23.

Ade, P. A. R. et al. (2015). Planck 2015 results. XVI. Isotropy and statistics of the CMB.

Aluri, P. K. and Jain, P. (2012). Large Scale Anisotropy due to Pre-Inﬂationary Phase of Cosmic
Evolution. Modern Physics Letters A, 27:1250014–1–1250014–11.

Aluri, P. K. and Jain, P. (2012). Parity Asymmetry in the CMBR Temperature Power Spectrum.
Mon. Not. Roy. Astron. Soc., 419:3378.

Aluri, P. K., Samal, P. K., Jain, P., and Ralston, J. P. (2011). Eﬀect of foregrounds on the
cosmic microwave background radiation multipole alignment. MNRAS, 414:1032–1046.

Beck, R. and Gaensler, B. M. (2004). Observations of magnetic ﬁelds in the Milky Way and in
nearby galaxies with a Square Kilometre Array. New Astronomy Reviews, 48:1289–1304.

Bennett, C. L. et al. (2011). Seven-Year Wilkinson Microwave Anisotropy Probe (WMAP)
Observations: Are There Cosmic Microwave Background Anomalies? Astrophys. J. Suppl.,
192:17.

Blake, C. and Wall, J. (2002). Detection of the velocity dipole in the radio galaxies of the nrao
vla sky survey. Nature, 416:150–152.

Brown, M. L. and Battye, R. A. (2011a). Mapping the Dark Matter with Polarized Radio
Surveys. ApJL, 735:L23.

Brown, M. L. and Battye, R. A. (2011b). Polarization as an indicator of intrinsic alignment in
radio weak lensing. MNRAS, 410:2057–2074.

Carroll, S. M., Tseng, C.-Y., and Wise, M. B. (2010). Translational invariance and the
anisotropy of the cosmic microwave background. Phys. Rev. D, 81:083501.

Condon, J. J., Cotton, W. D., Greisen, E. W., Yin, Q. F., Perley, R. A., Taylor, G. B., and
Broderick, J. J. (1998). The NRAO VLA Sky Survey. AJ, 115(5):1693–1716.

Copi, C. J., Huterer, D., Schwarz, D. J., and Starkman, G. D. (2007). Uncorrelated universe:
Statistical anisotropy and the vanishing angular correlation function in WMAP years 1 3.
Physical Review D., 75(2):023507.

Cruz, M., Martinez-Gonzalez, E., Vielva, P., and Cayon, L. (2005). Detection of a non-gaussian
spot in wmap. Mon. Not. Roy. Astron. Soc., 356:29–40.

de Oliveira-Costa, A., Tegmark, M., Zaldarriaga, M., and Hamilton, A. (2004). The Signiﬁcance
of the largest scale CMB ﬂuctuations in WMAP. Phys. Rev., D69:063516.

Dekel, A. and Lahav, O. (1999). Stochastic Nonlinear Galaxy Biasing. ApJ, 520:24–34.

Demetroullas, C. and Brown, M. L. (2016). Cross-correlation cosmic shear with the SDSS and
VLA FIRST surveys. MNRAS, 456:3100–3118.

16

Dewdney, P., Turner, W., Millenaar, R., McCool, R., Lazio, J., and Cornwell, T. (2013). Ska1
system baseline design. Document number SKA-TEL-SKO-DD-001 Revision, 1(1).

Dolag, K., Bartelmann, M., and Lesch, H. (2002). Evolution and structure of magnetic ﬁelds
in simulated galaxy clusters. A&A, 387:383–395.

Ellis, G. F. R. and Baldwin, J. E. (1984). On the Expected Anisotropy of Radio Source Counts.
MNRAS, 206:377–381.

Eriksen, H. K., Banday, A. J., Gorski, K. M., Hansen, F. K., and Lilje, P. B. (2007). Hemispher-
ical power asymmetry in the three-year Wilkinson Microwave Anisotropy Probe sky maps.
Astrophys. J., 660:L81–L84.

Fern´andez-Cobos, R., Vielva, P., Pietrobon, D., Balbi, A., Mart´ınez-Gonz´alez, E., and Barreiro,
R. B. (2014). Searching for a dipole modulation in the large-scale structure of the Universe.
Mon. Not. Roy. Astron. Soc., 441(3):2392–2397.

Ghosh, S., Kothari, R., Jain, P., and Rath, P. K. (2016). Dipole Modulation of Cosmic Mi-
crowave Background Temperature and Polarization. JCAP, 1601(01):046.

Gibelyou, C. and Huterer, D. (2012). Dipoles in the Sky. Mon. Not. Roy. Astron. Soc., 427:1994–
2021.

Gordon, C. (2007). Broken Isotropy from a Linear Modulation of the Primordial Perturbations.
Astrophys. J., 656:636–640.

Hajian, A., Souradeep, T., and Cornish, N. (2005). Statistical Isotropy of the Wilkinson Mi-
crowave Anisotropy Probe Data: A Bipolar Power Spectrum Analysis. ApJL, 618:L63–L66.

Hansen, F. K., Banday, A. J., and Gorski, K. M. (2004). Testing the cosmological principle of
isotropy: Local power spectrum estimates of the WMAP data. Mon. Not. Roy. Astron. Soc.,
354:641–665.

Haverkorn, M., Akahori, T., Carretti, E., Ferri`ere, K., Frick, P., Gaensler, B., Heald, G.,
Johnston-Hollitt, M., Jones, D., Landecker, T., Mao, S. A., Noutsos, A., Oppermann, N.,
Reich, W., Robishaw, T., Scaife, A., Schnitzeler, D., Stepanov, R., Sun, X., and Taylor, R.
(2015). Measuring magnetism in the Milky Way with the Square Kilometre Array. Advancing
Astrophysics with the Square Kilometre Array (AASKA14), page 96.

Hinshaw, G. et al. (2009). Five-Year Wilkinson Microwave Anisotropy Probe (WMAP) Obser-
vations: Data Processing, Sky Maps, and Basic Results. Astrophys. J. Suppl., 180:225–245.

Hirata, C. M. (2009). Constraints on cosmic hemispherical power anomalies from quasars.
JCAP, 0909:011.

Hoftuft, J., Eriksen, H. K., Banday, A. J., Gorski, K. M., Hansen, F. K., and Lilje, P. B.
(2009). Increasing evidence for hemispherical power asymmetry in the ﬁve-year WMAP
data. Astrophys. J., 699:985–989.

Hutsemekers, D. (1998). Evidence for very large-scale coherent orientations of quasar polariza-
tion vectors. A&A, 332:410–428.

Itoh, Y., Yahata, K., and Takada, M. (2010). A dipole anisotropy of galaxy distribution: Does
the CMB rest-frame exist in the local universe? Phys. Rev., D82:043530.

Jain, P., Narain, G., and Sarala, S. (2004). Large scale alignment of optical polarizations from
distant QSOs using coordinate invariant statistics. Mon. Not. Roy. Astron. Soc., 347:394.

17

Jain, P. and Ralston, J. P. (1999). Anisotropy in the Propagation of Radio Polarizations from
Cosmologically Distant Galaxies. Modern Physics Letters A, 14:417–432.

Jain, P. and Rath, P. K. (2015). Noncommutative Geometry and the Primordial Dipolar Imag-
inary Power Spectrum. Eur. Phys. J., C75:113.

Jain, P. and Sarala, S. (2006). Interpretation of the global anisotropy in the radio polarizations
of cosmologically distant sources. J. Astrophys. Astron., 27:443–454.

Kim, J. and Naselsky, P. (2010). Anomalous parity asymmetry of the Wilkinson Microwave
Anisotropy Probe power spectrum data at low multipoles. Astrophys. J., 714:L265–L267.

Kogut, A. et al. (1993). Dipole anisotropy in the COBE DMR ﬁrst year sky maps. Astrophys.
J., 419:1.

Kothari, R., Ghosh, S., Rath, P. K., Kashyap, G., and Jain, P. (2015a). Imprint of Inhomoge-
neous and Anisotropic Primordial Power Spectrum on CMB Polarization.

Kothari, R., Rath, P. K., and Jain, P. (2015b). Cosmological Power Spectrum in Non-
commutative Space-time.

Peebles, P. J. E. (1980). The large-scale structure of the universe.

Pelgrims, V. and Hutsem´ekers, D. (2015). Polarization alignments of radio quasars in
JVAS/CLASS surveys. MNRAS, 450:4161–4173.

Prunet, S., Uzan, J.-P., Bernardeau, F., and Brunier, T. (2005). Constraints on mode couplings
and modulation of the CMB with WMAP data. Phys. Rev. D, 71(8):083508.

Ralston, J. P. and Jain, P. (2004). The Virgo alignment puzzle in propagation of radiation on
cosmological scales. Int. J. Mod. Phys., D13:1857–1878.

Rath, P. K., Aluri, P. K., and Jain, P. (2015). Relating the inhomogeneous power spectrum to
the CMB hemispherical anisotropy. Phys. Rev., D91:023515.

Rath, P. K. and Jain, P. (2013). Testing the Dipole Modulation Model in CMBR. JCAP,
1312:014.

Rath, P. K., Mudholkar, T., Jain, P., Aluri, P. K., and Panda, S. (2013). Direction dependence
of the power spectrum and its eﬀect on the Cosmic Microwave Background Radiation. JCAP,
1304:007.

Rubart, M. and Schwarz, D. J. (2013). Cosmic radio dipole from NVSS and WENSS. Astron.
Astrophys., 555:A117.

Samal, P. K., Saha, R., Jain, P., and Ralston, J. P. (2008). Testing Isotropy of Cosmic Microwave
Background Radiation. Mon. Not. Roy. Astron. Soc., 385:1718.

Samal, P. K., Saha, R., Jain, P., and Ralston, J. P. (2009). Signals of Statistical Anisotropy in
WMAP Foreground-Cleaned Maps. Mon. Not. Roy. Astron. Soc., 396:511.

Sarala, S. and Jain, P. (2002). A Circular Statistical Method for Extracting Rotation Measures.
Journal of Astrophysics and Astronomy, 23:137.

Schwarz, D. J., Bacon, D., Chen, S., Clarkson, C., Huterer, D., Kunz, M., Maartens, R., Rac-
canelli, A., Rubart, M., and Starck, J.-L. (2015). Testing foundations of modern cosmology
with SKA all-sky surveys. PoS, AASKA14:032.

18

Shurtleﬀ, R. (2014). Testing the Alignment Tendency of Some Polarized Radio Sources.
arXiv:1408.2514.

Singal, A. K. (2011). Large peculiar motion of the solar system from the dipole anisotropy in
sky brightness due to distant radio sources. Astrophys. J., 742:L23.

Tiwari, P. and Jain, P. (2013). Polarization Alignment in JVAS/CLASS ﬂat spectrum radio
surveys. Int. J. Mod. Phys., D22(14):1350089.

Tiwari, P. and Jain, P. (2015a). Dipole Anisotropy in Integrated Linearly Polarized Flux Density
in NVSS Data. MNRAS, 447:2658–2670.

Tiwari, P. and Jain, P. (2015b). Extracting Spectral Index of Intergalactic Magnetic Field from
Radio Polarizations. ArXiv e-prints.

Tiwari, P., Kothari, R., Naskar, A., Nadkarni-Ghosh, S., and Jain, P. (2015). Dipole anisotropy
in sky brightness and source count distribution in radio NVSS data. Astropart. Phys., 61:1–11.

Tiwari, P. and Nusser, A. (2015). Revisiting the NVSS number count dipole. arXiv:1509.02532.

Wald, R. M. (1983). Asymptotic behavior of homogeneous cosmological models in the presence
of a positive cosmological constant. Physical Review D., 28:2118–2120.

Wilman, R. J., Miller, L., Jarvis, M. J., Mauch, T., Levrier, F., Abdalla, F. B., Rawlings,
S., Kl¨ockner, H.-R., Obreschkow, D., Olteanu, D., and Young, S. (2008). A semi-empirical
simulation of the extragalactic radio continuum sky for next generation radio telescopes.
Monthly Notices of the Royal Astronomical Society, 388(3):1335–1348.

Yoon, M., Huterer, D., Gibelyou, C., Kov´acs, A., and Szapudi, I. (2014). Dipolar modulation
in number counts of WISE-2MASS sources. Mon. Not. Roy. Astron. Soc., 445:L60–L64.

19
