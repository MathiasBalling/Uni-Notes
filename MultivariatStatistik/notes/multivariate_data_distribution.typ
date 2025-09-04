= Multivariate data and multivariate normal distribution

== 2D bivariate random vector
$ X = vec(delim: "[", x_1, x_2) $
Simultaneous pdf $f(x_1,x_2)=P(X_1=x_1,X_2=x_2)$ complete information.

Marginal PDFs $ f(x_1)=integral f(x_1, x_2)dif x_2 " and " f(x_2)=integral f(x_1,x_2) dif x_1 $


Mean vector $ mu = vec(E[x_1], E[x_2]) = vec(mu_1, mu_2) $

Marginal variances
$ sigma_1^2= sigma_11 = E[(X_1-mu_1)^2] >=0 $
$ sigma_2^2= sigma_22 = E[(X_2-mu_2)^2] >=0 $

Covariance
$ sigma_12 = "Cov"(X_1, X_2) = sigma_21 = E[(X_1-mu_1)(X_2-mu_2)] $

Covariance matrix
$ sum mat(delim: "[", sigma_1^2, sigma_12; sigma_12, sigma_2^2) $
The matrix is symmetric and has positive semi-definite eigenvalues $lambda_1,lambda_2 >=0$

Correlation coefficient $ rho_12 = sigma_12/(sigma_1 sigma_2) $

Correlation matrix $ rho= mat(delim: "[", 1, rho_12; rho_12, 1) $
$ -1 <= rho_12 <= 1 $

Generalized variance
$ abs(sum) = det(sum)=product_(i=1)^2 lambda_i $

Measure of amount of random variation

== pD bivariate random vector
$ X=[x_1,x_2,dots,x_p]^T $

Mean vector $ mu= vec(mu_1, dots, mu_p) $

Covariance matrix $ sum_(p times p)= mat(delim: "[", sigma_1^2, sigma_12, sigma_(1p); dots, sigma_2, dots; dots, dots, sigma_p) = E[(X-mu)(X-mu)^T] $

Correlation matrix:
$
  rho_(p times p) = mat(delim: "[", 1, rho_12, dots, rho_(1 p); dots, 1, dots, dots; dots, dots, 1, dots; dots, dots, dots, 1) -1 <=rho_(i j) <= 1
$

== Sampling
From a random sample we want to estimate the moment of the population ($mu, sum, rho$).

Data Matrix:
(Make = over X)
$
  X_(n times p) = mat(delim: "[", x_11, x_12, dots, x_(1 p); x_21, x_22, dots, x_(2 p); x_(n 1), x_(n 2), dots, x_(n p))= vec(delim: "[", x_1^T, x_2^T, dots, x_n^T)
$
Columns are the variables and rows are the observations.


== Descriptive statistics
Estimation of moments ($mu, sum, rho$)

$ hat(mu)=macron(x)=1/n sum_(j=1)^n X_j $
```matlab
% Matlab
mean(X)
```

$
  hat(sum)_(p times p) =S_(p times p) = 1/(n-1) sum_(j=1)^n (X_j-hat(mu))(X_j-hat(mu))^T=mat(s_1^2, s_12, dots, s_(1 p); dots, s_2^2, dots, dots; dots, dots, s_3^2, dots; dots, dots, dots, s_p^2)
$

```matlab
% Matlab
cov(X)
```


$
  hat(rho) = R = mat(1, r_12, r_13, dots, r_(1 p); dots, 1, dots, dots, dots; dots, dots, 1, dots, dots; dots, dots, dots, 1, dots; dots, dots, dots, dots, 1)
$
```matlab
% Matlab
corrcoef(X)
```
