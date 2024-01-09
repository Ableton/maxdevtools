# Don't do UI updates in the scheduler

Any calculations done in the timing-accurate scheduler thread in Max, when used in Live, will contribute to the CPU load of Live's audio thread, and add to Live's CPU indicator. Typically, events coming in from MIDI input objects or from the metro object will happen in the scheduler thread. This is because we need accurate timing when MIDI notes result in audio in Max Instruments or are passed on through Max MIDI Effects.

However, for UI animations we don't need this accuracy. We want as little calculation done in the scheduler thread as possible, so as soon as MIDI notes or repeated bangs are used only for the UI, we need to defer them, either with `[defer]` or `[deferlow]` or with `[qlim]` or `[qmetro]`. This way they will be done in Live's interface thread and only contribute to the interface updates getting a little slower.

## Example

![UI updates](ui-updates-example.gif)

```
<pre><code>
----------begin_max5_patcher----------
919.3ocyXtriSCCEFdc6SgU1fDTB9RthfEHXIKXCqPiF4IwTLp0Nj3LLHDu6
3XmLWfNvoTafEMQ10I+9ymSN9O4qqWkbg9JwPB5on2gVs5qqWsx00TGqlauJ
YO+plc7A2vRZz62KTljM9+yHtx35+YOG8Js5AFz3f.wQ6EldM5ChdaiAjzf9
rb2NDusEYznWKuT7fAzKFakZzKeyasWCeqHE8V2k9I+0JUCFAuMcQocRknQO
pbxQm6TMtWp1ILt4FYtSYqaFou3iOlVkbyH0ilkghm6siaZ9fTs87dQiwuLP
njT7FTd9zQVQk6DKEiNa5R9150SG1.b0RI9rcZ7SKVc8hNgpEQP3zx7DnvTb
XXVFpuKyW5DdRRRPm8K3rxS3DaaPU0SGozvx4ir7cX7nG.O7Qh262o4FHLRK
w9fYLX7IHZJXDIQCQlO.VmlGdDenMLBFQZrPjTwhGh1nH9HfjEMHybPxhxii
txmhdDFQpqOHq4Gf0rCyZ18wpbZ2Aawm4eSMg.NwcphFCvGjJvEYyi1inD2F
Kzr+4UZI0AmwbOUE0+eTnkTEKBYUwqHzhs.rMXRAaKfTFRaAdLipq.6Rc6dw
v.hkRxH40LvjFTCPLL9VEdHDVLX8gGSRa3K8rvXV1+GtCHzH8bIYdiiSiPid
61cBnoiWWioi2ysuzhn+bghewNwseCCfb961kbgxasCRVnKuRNBGPEwJNlQ+
a3+At8mH69YlZh6TY9+XyOrXsqIAGOqO9OW.CC179QB4Eb0V.L5+fA4ml0m2
OpZLRM3.F43KAsj45DU1bdyX+kB.Q4akTe2UjV8dtMEa5Njh+sFKJ84.y6KM
c55aDussSaefY96QM4AZi8XccANujwppYYkjJaWabe1D2+UjUUUQKJI1API1
ttyxt6V69xQ+v23xM+l5+twhA8XeyB1KaIitYF1JFLRE2EgtYPSuxKhb8fz8
shd25+AS.fJMEhxY2YPgR4B.RSR9wE6+.gvPXrHDJwfFGOYkxfnDKDJAJCIO
DJQfnDNDJA54sPj6AIgX5sHOYgVtI+ZkpCgR0PTpLDJU9WpBAATonPjiCpRO
4dpzSNIoKfp7IyHjJFgnzDjT9fTrEfN2yVjmVHCRQ9edeKucDdW2kh9g4A6j
vZB7iZ2zpZiqoT4aV3Z1KtTtLdmCqDdu0dkw5sZr2MsRtpv+hJI60V.UixYF
svsd1qmxZPbni64v4Cc82V+cc1gXi.
-----------end_max5_patcher-----------
</code></pre>
```