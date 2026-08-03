## different tests behaviour depending on TESTS_SUCCESS variable

TESTS_SUCCESS behaviour
- `always` all tests are passing
- `never` all tests are  (FAILED)
- `broken` fixture throws exception (BROKEN)
- `random` or not set – 10-20% probability of failure in asserts


## managin number of fixtures in unit-xxx

```shell
export TESTS_FIXTURES_COUNT=5
```




```shell
export TESTS_SUCCESS=random; ./runallure3.sh
export TESTS_SUCCESS=always; ./runallure3.sh
export TESTS_SUCCESS=broken; ./runallure3.sh
export TESTS_SUCCESS=always; ./runtests.sh 276
export TESTS_SUCCESS=random; ./runtests.sh
export TESTS_SUCCESS=broken; ./runtests.sh




export TESTS_SUCCESS=always; ./runtests.sh 276
export TESTS_SUCCESS=never; ./runtests.sh 276

```

```shell
export ALLURE_UPLOAD_RATE_WINDOW=0.75s
export ALLURE_UPLOAD_MAX_REQUESTS_PER_WINDOW=5
export ALLURE_UPLOAD_MAX_FILES_PER_WINDOW=100
export ALLURE_UPLOAD_MAX_BYTES_PER_WINDOW=536870912

export TESTS_SUCCESS=always

export TESTS_FIXTURES_COUNT=5
```