import json

data = [
{"d":"2026-03-02","omxspi":1094.66,"omxspi_ret":None,"vix":21.44,"us10y":4.05,"eursek":10.708},
{"d":"2026-03-03","omxspi":1065.46,"omxspi_ret":-2.6675,"vix":23.57,"us10y":4.06,"eursek":10.7265},
{"d":"2026-03-04","omxspi":1079.61,"omxspi_ret":1.3281,"vix":21.15,"us10y":4.09,"eursek":10.6785},
{"d":"2026-03-05","omxspi":1068.41,"omxspi_ret":-1.0374,"vix":23.75,"us10y":4.13,"eursek":10.6885},
{"d":"2026-03-06","omxspi":1057.55,"omxspi_ret":-1.0165,"vix":29.49,"us10y":4.15,"eursek":10.693},
{"d":"2026-03-09","omxspi":1039.96,"omxspi_ret":-1.6633,"vix":25.50,"us10y":4.12,"eursek":10.6945},
{"d":"2026-03-10","omxspi":1068.48,"omxspi_ret":2.7424,"vix":24.93,"us10y":4.15,"eursek":10.606},
{"d":"2026-03-11","omxspi":1060.01,"omxspi_ret":-0.7927,"vix":24.23,"us10y":4.21,"eursek":10.6543},
{"d":"2026-03-12","omxspi":1060.77,"omxspi_ret":0.0717,"vix":27.29,"us10y":4.27,"eursek":10.7108},
{"d":"2026-03-13","omxspi":1047.14,"omxspi_ret":-1.2849,"vix":27.19,"us10y":4.28,"eursek":10.7545},
{"d":"2026-03-16","omxspi":1050.37,"omxspi_ret":0.3085,"vix":23.51,"us10y":4.23,"eursek":10.769},
{"d":"2026-03-17","omxspi":1049.77,"omxspi_ret":-0.0571,"vix":22.37,"us10y":4.20,"eursek":10.7055},
{"d":"2026-03-18","omxspi":1046.63,"omxspi_ret":-0.2991,"vix":25.09,"us10y":4.26,"eursek":10.7778},
{"d":"2026-03-19","omxspi":1012.22,"omxspi_ret":-3.2877,"vix":24.06,"us10y":4.25,"eursek":10.8065},
{"d":"2026-03-20","omxspi":996.43,"omxspi_ret":-1.5599,"vix":26.78,"us10y":4.39,"eursek":10.7825},
{"d":"2026-03-23","omxspi":1003.57,"omxspi_ret":0.7166,"vix":26.15,"us10y":4.34,"eursek":10.8328},
{"d":"2026-03-24","omxspi":1007.77,"omxspi_ret":0.4185,"vix":26.95,"us10y":4.39,"eursek":10.8238},
{"d":"2026-03-25","omxspi":1021.17,"omxspi_ret":1.3297,"vix":25.33,"us10y":4.33,"eursek":10.7715},
{"d":"2026-03-26","omxspi":1007.8,"omxspi_ret":-1.3093,"vix":27.44,"us10y":4.42,"eursek":10.8405},
{"d":"2026-03-27","omxspi":997.42,"omxspi_ret":-1.0300,"vix":31.05,"us10y":4.44,"eursek":10.878},
{"d":"2026-03-30","omxspi":1007.8,"omxspi_ret":1.0407,"vix":30.61,"us10y":4.35,"eursek":10.906},
{"d":"2026-03-31","omxspi":1022.26,"omxspi_ret":1.4348,"vix":25.25,"us10y":4.30,"eursek":10.943},
{"d":"2026-04-01","omxspi":1048.77,"omxspi_ret":2.5933,"vix":24.54,"us10y":4.33,"eursek":10.888},
{"d":"2026-04-02","omxspi":1034.3,"omxspi_ret":-1.3797,"vix":23.87,"us10y":4.31,"eursek":10.948},
{"d":"2026-04-07","omxspi":1033.73,"omxspi_ret":-0.0551,"vix":25.78,"us10y":4.33,"eursek":10.99},
{"d":"2026-04-08","omxspi":1074.22,"omxspi_ret":3.9169,"vix":21.04,"us10y":4.29,"eursek":10.784},
{"d":"2026-04-09","omxspi":1069.5,"omxspi_ret":-0.4394,"vix":19.49,"us10y":4.29,"eursek":10.8765},
{"d":"2026-04-10","omxspi":1080.23,"omxspi_ret":1.0033,"vix":19.23,"us10y":4.31,"eursek":10.836},
{"d":"2026-04-13","omxspi":1079.71,"omxspi_ret":-0.0481,"vix":19.12,"us10y":4.30,"eursek":10.892},
{"d":"2026-04-14","omxspi":1091.8,"omxspi_ret":1.1197,"vix":18.36,"us10y":4.26,"eursek":10.798},
{"d":"2026-04-15","omxspi":1090.98,"omxspi_ret":-0.0751,"vix":18.17,"us10y":4.29,"eursek":10.85},
{"d":"2026-04-16","omxspi":1095.55,"omxspi_ret":0.4189,"vix":17.94,"us10y":4.32,"eursek":10.804},
{"d":"2026-04-17","omxspi":1117.99,"omxspi_ret":2.0483,"vix":17.48,"us10y":4.26,"eursek":10.803},
{"d":"2026-04-20","omxspi":1107.89,"omxspi_ret":-0.9034,"vix":18.87,"us10y":4.26,"eursek":10.7685},
{"d":"2026-04-21","omxspi":1101.37,"omxspi_ret":-0.5885,"vix":19.50,"us10y":4.30,"eursek":10.7495},
{"d":"2026-04-22","omxspi":1097.14,"omxspi_ret":-0.3841,"vix":18.92,"us10y":4.30,"eursek":10.776},
{"d":"2026-04-23","omxspi":1093.73,"omxspi_ret":-0.3108,"vix":19.31,"us10y":4.34,"eursek":10.7795},
{"d":"2026-04-24","omxspi":1083.16,"omxspi_ret":-0.9664,"vix":18.71,"us10y":4.31,"eursek":10.82},
{"d":"2026-04-27","omxspi":1074.2,"omxspi_ret":-0.8272,"vix":18.02,"us10y":4.35,"eursek":10.7885},
{"d":"2026-04-28","omxspi":1064.25,"omxspi_ret":-0.9263,"vix":17.83,"us10y":4.36,"eursek":10.8485},
{"d":"2026-04-29","omxspi":1058.07,"omxspi_ret":-0.5807,"vix":18.81,"us10y":4.42,"eursek":10.8405},
{"d":"2026-04-30","omxspi":1064.23,"omxspi_ret":0.5822,"vix":16.89,"us10y":4.40,"eursek":10.8555},
{"d":"2026-05-04","omxspi":1057.28,"omxspi_ret":-0.6531,"vix":18.29,"us10y":4.45,"eursek":10.835},
{"d":"2026-05-05","omxspi":1069.07,"omxspi_ret":1.1151,"vix":17.38,"us10y":4.43,"eursek":10.84},
{"d":"2026-05-06","omxspi":1097.97,"omxspi_ret":2.7033,"vix":17.39,"us10y":4.36,"eursek":10.8335},
{"d":"2026-05-07","omxspi":1085.39,"omxspi_ret":-1.1458,"vix":17.08,"us10y":4.41,"eursek":10.825},
{"d":"2026-05-08","omxspi":1073.8,"omxspi_ret":-1.0678,"vix":17.19,"us10y":4.38,"eursek":10.842},
{"d":"2026-05-11","omxspi":1077.32,"omxspi_ret":0.3278,"vix":18.38,"us10y":4.42,"eursek":10.8765},
{"d":"2026-05-12","omxspi":1062.09,"omxspi_ret":-1.4137,"vix":17.99,"us10y":4.46,"eursek":10.8935},
{"d":"2026-05-13","omxspi":1064.2,"omxspi_ret":0.1987,"vix":17.87,"us10y":4.46,"eursek":10.915},
{"d":"2026-05-15","omxspi":1060.8,"omxspi_ret":-0.3195,"vix":18.43,"us10y":4.59,"eursek":10.982},
{"d":"2026-05-18","omxspi":1065.26,"omxspi_ret":0.4204,"vix":17.82,"us10y":4.61,"eursek":10.9465},
{"d":"2026-05-19","omxspi":1069.17,"omxspi_ret":0.3670,"vix":18.06,"us10y":4.67,"eursek":10.909},
{"d":"2026-05-20","omxspi":1083.52,"omxspi_ret":1.3422,"vix":17.44,"us10y":4.57,"eursek":10.8775},
{"d":"2026-05-21","omxspi":1087.45,"omxspi_ret":0.3627,"vix":16.76,"us10y":4.57,"eursek":10.8615},
{"d":"2026-05-22","omxspi":1097.74,"omxspi_ret":0.9463,"vix":16.70,"us10y":4.56,"eursek":10.8695},
{"d":"2026-05-25","omxspi":1114.13,"omxspi_ret":1.4931,"vix":16.59,"us10y":None,"eursek":10.7965},
{"d":"2026-05-26","omxspi":1103.44,"omxspi_ret":-0.9595,"vix":17.01,"us10y":4.50,"eursek":10.8245},
{"d":"2026-05-27","omxspi":1101.57,"omxspi_ret":-0.1695,"vix":16.29,"us10y":4.48,"eursek":10.7895},
{"d":"2026-05-28","omxspi":1089.85,"omxspi_ret":-1.0639,"vix":15.74,"us10y":4.45,"eursek":10.8215},
{"d":"2026-05-29","omxspi":1095.31,"omxspi_ret":0.5010,"vix":15.32,"us10y":4.45,"eursek":10.772},
{"d":"2026-06-01","omxspi":1078.29,"omxspi_ret":-1.5539,"vix":16.05,"us10y":4.47,"eursek":10.789},
{"d":"2026-06-02","omxspi":1094.56,"omxspi_ret":1.5089,"vix":15.77,"us10y":4.46,"eursek":10.825},
{"d":"2026-06-03","omxspi":1089.39,"omxspi_ret":-0.4723,"vix":16.06,"us10y":4.49,"eursek":10.884},
{"d":"2026-06-04","omxspi":1092.23,"omxspi_ret":0.2607,"vix":15.40,"us10y":4.47,"eursek":10.8803},
{"d":"2026-06-05","omxspi":1085.28,"omxspi_ret":-0.6363,"vix":21.51,"us10y":4.55,"eursek":10.8675},
{"d":"2026-06-08","omxspi":1083.47,"omxspi_ret":-0.1668,"vix":18.92,"us10y":4.56,"eursek":10.876},
{"d":"2026-06-09","omxspi":1071.24,"omxspi_ret":-1.1288,"vix":19.87,"us10y":4.53,"eursek":10.885},
{"d":"2026-06-10","omxspi":1068.34,"omxspi_ret":-0.2707,"vix":22.22,"us10y":4.55,"eursek":10.9655},
{"d":"2026-06-11","omxspi":1069.98,"omxspi_ret":0.1535,"vix":19.44,"us10y":4.45,"eursek":10.9935},
{"d":"2026-06-12","omxspi":1086.96,"omxspi_ret":1.5869,"vix":17.68,"us10y":4.48,"eursek":10.928},
{"d":"2026-06-15","omxspi":1090.43,"omxspi_ret":0.3192,"vix":16.20,"us10y":4.47,"eursek":10.8975},
{"d":"2026-06-16","omxspi":1089.19,"omxspi_ret":-0.1137,"vix":16.41,"us10y":4.43,"eursek":10.897},
{"d":"2026-06-17","omxspi":1091.71,"omxspi_ret":0.2314,"vix":18.44,"us10y":4.49,"eursek":10.891},
{"d":"2026-06-18","omxspi":1093.8,"omxspi_ret":0.1914,"vix":16.40,"us10y":4.46,"eursek":10.9845},
{"d":"2026-06-22","omxspi":1095.69,"omxspi_ret":0.1728,"vix":17.28,"us10y":4.51,"eursek":10.998},
{"d":"2026-06-23","omxspi":1082.86,"omxspi_ret":-1.1710,"vix":19.49,"us10y":4.50,"eursek":11.0585},
{"d":"2026-06-24","omxspi":1085.47,"omxspi_ret":0.2410,"vix":18.63,"us10y":4.41,"eursek":11.085},
{"d":"2026-06-25","omxspi":1094.7,"omxspi_ret":0.8503,"vix":18.89,"us10y":4.40,"eursek":11.069},
{"d":"2026-06-26","omxspi":1086.53,"omxspi_ret":-0.7463,"vix":18.41,"us10y":4.38,"eursek":11.0775},
{"d":"2026-06-29","omxspi":1090.0,"omxspi_ret":0.3194,"vix":17.65,"us10y":4.38,"eursek":11.0865},
{"d":"2026-06-30","omxspi":1101.54,"omxspi_ret":1.0587,"vix":16.45,"us10y":4.44,"eursek":11.0935},
{"d":"2026-07-01","omxspi":1098.94,"omxspi_ret":-0.2360,"vix":16.59,"us10y":4.48,"eursek":11.0955},
{"d":"2026-07-02","omxspi":1109.7,"omxspi_ret":0.9791,"vix":16.15,"us10y":4.49,"eursek":11.0775},
{"d":"2026-07-03","omxspi":1122.63,"omxspi_ret":1.1652,"vix":15.81,"us10y":None,"eursek":11.0315},
{"d":"2026-07-06","omxspi":1117.8,"omxspi_ret":-0.4302,"vix":15.57,"us10y":4.48,"eursek":11.015},
{"d":"2026-07-07","omxspi":1108.69,"omxspi_ret":-0.8150,"vix":16.13,"us10y":4.55,"eursek":11.0443},
{"d":"2026-07-08","omxspi":1085.4,"omxspi_ret":-2.1007,"vix":16.90,"us10y":4.56,"eursek":11.0565},
{"d":"2026-07-09","omxspi":1100.63,"omxspi_ret":1.4032,"vix":15.84,"us10y":4.54,"eursek":11.062},
{"d":"2026-07-10","omxspi":1099.59,"omxspi_ret":-0.0945,"vix":15.03,"us10y":4.56,"eursek":11.0145},
{"d":"2026-07-13","omxspi":1096.64,"omxspi_ret":-0.2683,"vix":17.16,"us10y":4.62,"eursek":11.027},
{"d":"2026-07-14","omxspi":1097.3,"omxspi_ret":0.0602,"vix":16.50,"us10y":4.58,"eursek":11.036},
{"d":"2026-07-15","omxspi":1095.84,"omxspi_ret":-0.1331,"vix":15.67,"us10y":4.55,"eursek":11.0473},
{"d":"2026-07-16","omxspi":1099.98,"omxspi_ret":0.3778,"vix":16.73,"us10y":4.57,"eursek":11.0285},
{"d":"2026-07-17","omxspi":1098.37,"omxspi_ret":-0.1464,"vix":18.77,"us10y":4.55,"eursek":11.0405},
{"d":"2026-07-20","omxspi":1092.96,"omxspi_ret":-0.4925,"vix":18.65,"us10y":4.60,"eursek":11.045},
{"d":"2026-07-21","omxspi":1095.3,"omxspi_ret":0.2141,"vix":17.05,"us10y":4.63,"eursek":11.0485},
{"d":"2026-07-22","omxspi":1107.47,"omxspi_ret":1.1111,"vix":16.64,"us10y":4.67,"eursek":11.0775},
{"d":"2026-07-23","omxspi":1098.28,"omxspi_ret":-0.8298,"vix":18.70,"us10y":4.71,"eursek":11.0955},
{"d":"2026-07-24","omxspi":1108.74,"omxspi_ret":0.9524,"vix":18.58,"us10y":4.69,"eursek":11.055},
{"d":"2026-07-27","omxspi":1116.28,"omxspi_ret":0.6801,"vix":18.67,"us10y":4.65,"eursek":11.0445},
{"d":"2026-07-28","omxspi":1121.09,"omxspi_ret":0.4309,"vix":18.21,"us10y":4.61,"eursek":11.0625},
{"d":"2026-07-29","omxspi":1119.18,"omxspi_ret":-0.1704,"vix":20.66,"us10y":4.67,"eursek":11.053},
{"d":"2026-07-30","omxspi":1123.08,"omxspi_ret":0.3485,"vix":17.09,"us10y":4.68,"eursek":11.0098},
{"d":"2026-07-31","omxspi":1125.61,"omxspi_ret":0.2253,"vix":15.99,"us10y":4.75,"eursek":10.9855},
{"d":"2026-08-03","omxspi":1134.86,"omxspi_ret":0.8218,"vix":15.86,"us10y":4.70,"eursek":10.9845},
{"d":"2026-08-04","omxspi":1150.18,"omxspi_ret":1.3499,"vix":16.50,"us10y":4.63,"eursek":10.9925},
{"d":"2026-08-05","omxspi":1149.13,"omxspi_ret":-0.0913,"vix":15.81,"us10y":4.63,"eursek":10.9635},
{"d":"2026-08-06","omxspi":1148.43,"omxspi_ret":-0.0609,"vix":15.15,"us10y":4.69,"eursek":10.9240},
{"d":"2026-08-07","omxspi":1146.65,"omxspi_ret":-0.1550,"vix":14.90,"us10y":4.65,"eursek":10.9455},
{"d":"2026-08-10","omxspi":1142.56,"omxspi_ret":-0.3567,"vix":15.46,"us10y":4.72,"eursek":10.9655},
{"d":"2026-08-11","omxspi":1140.22,"omxspi_ret":-0.2048,"vix":15.28,"us10y":4.70,"eursek":10.9635},
{"d":"2026-08-12","omxspi":1139.14,"omxspi_ret":-0.0947,"vix":14.55,"us10y":4.68,"eursek":10.9965},
{"d":"2026-08-13","omxspi":1137.51,"omxspi_ret":-0.1431,"vix":14.63,"us10y":4.63,"eursek":11.0285},
{"d":"2026-08-14","omxspi":1135.86,"omxspi_ret":-0.1451,"vix":14.25,"us10y":4.68,"eursek":10.9990},
{"d":"2026-08-17","omxspi":1131.79,"omxspi_ret":-0.3583,"vix":15.19,"us10y":4.72,"eursek":11.0010},
{"d":"2026-08-18","omxspi":1125.91,"omxspi_ret":-0.5195,"vix":15.84,"us10y":4.71,"eursek":11.0260},
]

import statistics

def pearson(x, y):
    n = len(x)
    mx, my = sum(x)/n, sum(y)/n
    cov = sum((a-mx)*(b-my) for a,b in zip(x,y))
    vx = sum((a-mx)**2 for a in x)
    vy = sum((b-my)**2 for b in y)
    return cov / (vx*vy)**0.5

# Build aligned series
dates = [r["d"] for r in data]
omxspi_ret = [r["omxspi_ret"] for r in data]
vix = [r["vix"] for r in data]
us10y = [r["us10y"] for r in data]
eursek = [r["eursek"] for r in data]

# VIX daily change (level diff), aligned to omxspi_ret (both start from index 1)
vix_chg = [vix[i]-vix[i-1] for i in range(1,len(vix))]
omx_ret2 = omxspi_ret[1:]  # skip first None

# 1. Correlation: VIX level change vs OMXSPI daily return
c1 = pearson(vix_chg, omx_ret2)

# 2. Correlation: VIX level vs OMXSPI level (non-stationary but still informative)
c2 = pearson(vix[1:], [r["omxspi"] for r in data][1:])

# 3. US10Y change vs OMXSPI return (only where us10y not None)
pairs = [(us10y[i]-us10y[i-1], omxspi_ret[i]) for i in range(1,len(data)) if us10y[i] is not None and us10y[i-1] is not None]
us10y_chg = [p[0] for p in pairs]
omx_for_us10y = [p[1] for p in pairs]
c3 = pearson(us10y_chg, omx_for_us10y)

# 4. EUR/SEK change vs OMXSPI return
eursek_chg = [eursek[i]-eursek[i-1] for i in range(1,len(eursek))]
c4 = pearson(eursek_chg, omx_ret2)

print(f"n = {len(omx_ret2)} trading days (Mar 3 - Aug 18, 2026)\n")
print(f"1. VIX daily change  vs OMXSPI daily return:  r = {c1:.3f}")
print(f"2. VIX level         vs OMXSPI level:          r = {c2:.3f}")
print(f"3. US10Y daily change vs OMXSPI daily return:  r = {c3:.3f}  (n={len(us10y_chg)})")
print(f"4. EUR/SEK daily chg vs OMXSPI daily return:   r = {c4:.3f}")

# Rolling 20-day correlation of VIX change vs OMXSPI return, to see if relationship is stable
window = 20
print(f"\nRolling {window}-day correlation (VIX chg vs OMXSPI ret):")
roll_dates = dates[1:]
for i in range(window, len(vix_chg)+1, 10):
    seg_vix = vix_chg[i-window:i]
    seg_omx = omx_ret2[i-window:i]
    r = pearson(seg_vix, seg_omx)
    print(f"  {roll_dates[i-window]} to {roll_dates[i-1]}: r = {r:.3f}")
