# EcustDiff

> DIY an Autodiff to challenge Fashion-MNIST

## What is Fashion-MNIST

See https://github.com/zalandoresearch/fashion-mnist/blob/master/README.zh-CN.md

Data available at `./data`.

(Dataset information: http://yann.lecun.com/exdb/mnist/)

## What is Autodiff

See Ref2.

Implementation: See Ref3 and `./ecust_autodiff`.

Test:

```bash
# sudo pip install nose
nosetests -v autodiff_test.py
```

## How

See `./notebook/mnist.ipynb`.

## Conclusion

We implement a simple reverse-mode autodiff library, and run a logistic regression on Fashion-MNIST.

What's more? We can implement a CNN classifier on Fashion-MNIST via EucstAutodiff. TBD.

## Reference

* https://github.com/zalandoresearch/fashion-mnist
* http://dlsys.cs.washington.edu/pdf/lecture4.pdf
* https://github.com/dlsys-course/assignment1
* https://github.com/camelop/learnMnist-dlsys