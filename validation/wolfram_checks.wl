(* Independent algebra checks. These do not certify physical realization. *)

weights = {0.005085, 0.984868, 0.010047};
weightCheck = Total[weights] == 1;

laneGrowth = FullSimplify[(n + 1) n - n (n - 1), Assumptions -> n >= 1 && Element[n, Integers]];

delta = 4.6692;
alpha = 0.0256831;
kernelSum = FullSimplify[
  Sum[delta^-j Exp[-alpha j t], {j, 0, Infinity}],
  Assumptions -> t >= 0
];
kernelBound = FullSimplify[kernelSum <= 1/(1 - 1/delta), Assumptions -> t >= 0];

laplacian = {{1, -1, 0}, {-1, 2, -1}, {0, -1, 1}};
q = Inverse[IdentityMatrix[3] + laplacian];
x = {2, -1, 4};
xp = q.x;
graphChecks = {
  SymmetricMatrixQ[q],
  Min[Eigenvalues[q]] > 0,
  Total[xp] == Total[x],
  Chop[xp.laplacian.xp - x.laplacian.x] <= 0
};

<|
  "WeightCheck" -> weightCheck,
  "LaneGrowth" -> laneGrowth,
  "KernelSum" -> kernelSum,
  "KernelBound" -> kernelBound,
  "GraphChecks" -> graphChecks
|>
