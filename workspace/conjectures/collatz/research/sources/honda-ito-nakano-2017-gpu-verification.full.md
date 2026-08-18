<!-- source: https://doi.org/10.15803/ijnc.7.1_69 | converted from HTML -->

GPU-accelerated Exhaustive Verification of the Collatz Conjecture

International Journal of Networking and Computing

Online ISSN : 2185-2847
Print ISSN : 2185-2839
ISSN-L : 2185-2839

- [Journal home][1]
- [All issues][2]
- [About the journal][3]

- [J-STAGE home][4]
- /
- [International Journal of Netwo ...][1]
- /
- [Volume 7 (2017) Issue 1][5]
- /
- Article overview

Regular Papers

GPU-accelerated Exhaustive Verification of the Collatz Conjecture

[Takumi Honda][6], [Yasuaki Ito][7], [Koji Nakano][8]

Author information

- Takumi Honda

Hiroshima University

- Yasuaki Ito

Hiroshima University

- Koji Nakano

Hiroshima University

#### Corresponding author

[image: ORCID]

Keywords: [Collatz conjecture][9], [GPGPU][10], [Parallel processing][11], [Exhaustive verification][12], [Coalesced access][13], [Bank conflict][14]

JOURNAL FREE ACCESS

2017 Volume 7 Issue 1 Pages 69-85

DOI [https://doi.org/10.15803/ijnc.7.1_69][15]

Details

- Published: 2017 Received: April 06, 2016 Available on J-STAGE: February 07, 2017 Accepted: July 04, 2016 Advance online publication: - Revised: June 15, 2016

[Download PDF (392K)][16]

Download citation [RIS][17]

(compatible with EndNote, Reference Manager, ProCite, RefWorks)

[BIB TEX][18]

(compatible with BibDesk, LaTeX)

Text

[How to download citation][19]

[Contact us][20]

Article overview

Share

- [21]
- [image: X] [22]
- [23]
- [24]

Abstract

The main contribution of this paper is to present an implementation that performs the exhaustive search to verify the Collatz conjecture using a GPU. Consider the following operation on an arbitrary positive number: if the number is even, divide it by two, and if the number is odd, triple it and add one. The Collatz conjecture asserts that, starting from any positive number m, repeated iteration of the operations eventually produces the value 1. We have implemented it on NVIDIA GeForce GTX TITAN X and evaluated the performance. The experimental results show that, our GPU implementation can verify 1.31×10 12 64-bit numbers per second. While the sequential CPU implementation on Intel Core i7-4790 can verify 5.25×10 9 64-bit numbers per second. Thus, our implementation on the GPU attains a speed-up factor of 249 over the sequential CPU implementation. Additionally, we accelerated the computation of counting the number of the above operations until a number reaches 1, called delay that is one of the mathematical interests for the Collatz conjecture by the GPU. Using a similar idea, we achieved a speed-up factor of 73.

References (20)

Related articles (0)

Figures (0)

Content from these authors

Supplementary material (0)

Result List ()

Cited by (2)

&copy; 2017 International Journal of Networking and Computing

[Previous article][25] [Next article][26]

Favorites & Alerts

- Add to favorites
- Additional info alert
- Citation alert
- Authentication alert

Related articles

Recently viewed articles

Share this page

- [21]
- [image: X] [22]
- [23]
- [24]

[feedback][27]

Top

**

### Register with J-STAGE for free!

[Register][28]

Already have an account? Sign in [here][29]


## Links

[1]: https://www.jstage.jst.go.jp/browse/ijnc/-char/en
[2]: https://www.jstage.jst.go.jp/browse/ijnc/list/-char/en
[3]: https://www.jstage.jst.go.jp/browse/ijnc/_pubinfo/-char/en
[4]: https://www.jstage.jst.go.jp/browse/-char/en
[5]: https://www.jstage.jst.go.jp/browse/ijnc/7/1/_contents/-char/en
[6]: https://www.jstage.jst.go.jp/search/global/_search/-char/en?item=8&word=Takumi+Honda
[7]: https://www.jstage.jst.go.jp/search/global/_search/-char/en?item=8&word=Yasuaki+Ito
[8]: https://www.jstage.jst.go.jp/search/global/_search/-char/en?item=8&word=Koji+Nakano
[9]: /search/global/_search/-char/en?item=5&word=Collatz+conjecture
[10]: /search/global/_search/-char/en?item=5&word=GPGPU
[11]: /search/global/_search/-char/en?item=5&word=Parallel+processing
[12]: /search/global/_search/-char/en?item=5&word=Exhaustive+verification
[13]: /search/global/_search/-char/en?item=5&word=Coalesced+access
[14]: /search/global/_search/-char/en?item=5&word=Bank+conflict
[15]: https://doi.org/10.15803/ijnc.7.1_69
[16]: https://www.jstage.jst.go.jp/article/ijnc/7/1/7_69/_pdf/-char/en
[17]: https://www.jstage.jst.go.jp/AF06S010ShoshJkuDld?sryCd=ijnc&noVol=7&noIssue=1&kijiCd=7_69&kijiLangKrke=en&kijiToolIdHkwtsh=AT0072&request_locale=EN
[18]: https://www.jstage.jst.go.jp/AF06S010ShoshJkuDld?sryCd=ijnc&noVol=7&noIssue=1&kijiCd=7_69&kijiLangKrke=en&kijiToolIdHkwtsh=AT0073&request_locale=EN
[19]: https://www.jstage.jst.go.jp/static/pages/HowToDownload/-char/en
[20]: https://www.jstage.jst.go.jp/browse/ijnc/_pubinfo/-char/en#information
[21]: https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fdoi.org%2F10.15803%2Fijnc.7.1_69
[22]: http://twitter.com/share?url=https%3A%2F%2Fdoi.org%2F10.15803%2Fijnc.7.1_69&text=J-STAGE+Articles+-+GPU-accelerated+Exhaustive+Verification+of+the+Collatz+Conjecture
[23]: mailto:?body=International%20Journal%20of%20Networking%20and%20Computing%0A%0AGPU-accelerated%20Exhaustive%20Verification%20of%20the%20Collatz%20Conjecture%0A%0Ahttps%3A%2F%2Fdoi.org%2F10.15803%2Fijnc.7.1_69%0A
[24]: http://www.mendeley.com/import/?doi=10.15803/ijnc.7.1_69
[25]: https://www.jstage.jst.go.jp/article/ijnc/7/1/7_50/_article/-char/en
[26]: https://www.jstage.jst.go.jp/article/ijnc/7/1/7_86/_article/-char/en
[27]: https://form2.jst.go.jp/s/jstage-feedback
[28]: /myregister/-char/en
[29]: /mylogin/-char/en?sourceurl=https%3A%2F%2Fwww.jstage.jst.go.jp%2Farticle%2Fijnc%2F7%2F1%2F7_69%2F_article%2F-char%2Fen
