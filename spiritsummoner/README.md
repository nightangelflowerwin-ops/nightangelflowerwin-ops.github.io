# Finding Wealth

A local dashboard for exploring steganography and cryptography through whole-word interpretations of Trithemius-inspired positional methods.

## Use

Download this repository and open `index.html` in Chrome or another modern browser. No installation or build step is required.

- Paste text or choose one of eight supplied isolated BIP39 sections.
- Explore 18 calculable methods and filter results by spirit.
- Inspect selected positions, counts, and full output order.
- Apply coordinate-digit positions to isolated sections.
- Choose cached OpenCage matches or enter a session-only API key for new place queries.
- Export experiments as JSON.

## Interpretation

Historical rules select initials. Substituting whole words, or filtering BIP39 vocabulary before selection, is a research hypothesis. Thirteen methods remain unresolved due to missing boundaries, source line layout, or verification. Outputs are not confirmed decipherments. This application does not test wallet checksums, derive keys, or query wallets.

Coordinates use digit + 10 × zero-based digit index, with one-based word positions. Missing positions are retained, never wrapped or deleted. The article's Supreme Court coordinates are preserved separately from live geocoding results. Country names do not identify an intended landmark.

## Privacy

Text remains in browser memory unless you explicitly export it. No API key is bundled or persisted. New OpenCage searches transmit only the place query and the API key to OpenCage. The spirit viewer and cached coordinates work offline.

## Sources and attribution

- [Article and coordinate example](https://medium.com/coinmonks/securing-bitcoin-seed-phrases-in-stories-d8eb43a02254)
- [Selenus historical scan](https://archive.org/details/gustaviselenicry00augu), Book III chapters 4–11
- [Latin Steganographia transcription](https://www.esotericarchives.com/tritheim/stegano.htm)
- [OpenCage API skill](https://github.com/OpenCageData/opencage-skills)
- [OpenCage and open-data attribution](https://opencagedata.com/credits)

Cached geographic results were retrieved on October 3, 2026. Neither a geocoder result nor a readable output establishes the puzzle's intended key.

## Validation

The position engine matched 144 reference section outputs. Permutation methods were checked for lengths 0–149. Coordinate tests reproduce the article's 12 reference positions and reject invalid axes. Startup and filtering were checked with a simulated document; full browser visual verification remains outstanding.
