import matplotlib.pyplot as plt
import scienceplots  # noqa: F401
import skdim
from sklearn import datasets

plt.style.use("science")

swiss_roll, sr_color = datasets.make_swiss_roll(
    n_samples=1000, noise=0.0, random_state=0
)
twin_peaks = skdim.datasets.hyperTwinPeaks(n=1000, d=2, height=1, random_state=0)


fig, (ax1, ax2) = plt.subplots(
    1,
    2,
    figsize=(5.91, 6),
    facecolor="white",
    tight_layout=True,
    subplot_kw={"projection": "3d"},
)

ax1.scatter(
    swiss_roll[:, 0], swiss_roll[:, 1], swiss_roll[:, 2], c=sr_color, alpha=0.8, s=50
)
ax1.view_init(azim=-70, elev=15)
ax1.xaxis.set_major_formatter(plt.NullFormatter())
ax1.zaxis.set_major_formatter(plt.NullFormatter())
ax1.yaxis.set_major_formatter(plt.NullFormatter())


ax2.scatter(
    twin_peaks[:, 0],
    twin_peaks[:, 1],
    twin_peaks[:, 2],
    c=twin_peaks[:, 2],
    alpha=0.8,
    s=50,
)
ax2.view_init(azim=-70, elev=15)
ax2.xaxis.set_major_formatter(plt.NullFormatter())
ax2.yaxis.set_major_formatter(plt.NullFormatter())
ax2.zaxis.set_major_formatter(plt.NullFormatter())

fig.set_size_inches(5.91, 3.5)
fig.savefig("./figures/artificial_datasets.pgf", backend="pgf")
