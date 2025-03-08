* 2021-01-10
	* `WeakRefObservableEvent` moved to `weakref`
	* Added: Decorator `@deprecated`

* 2021-01-11
	* Added: `TerminationFlag`
	* Added: `InterruptedException`
	* Added: `TimeStamp`

* 2021-01-13
	* Added: `duration` subcomponent

* 2021-02-16
	* Added: `deferred` with `run()`

* 2021-06-29
	* Bugfix: Allow `None` for a logger in `runProcessAsOtherUser()`
	* Added: Support for milliseconds in `formatTime()`
	* Refactored: `T1`, `T5`, `D`
	* Added: `TApprox`

* 2021-12-03
	* Added: octal support in `ChModValue`

* 2021-12-14
	* Improved: Compatibility to non-POSIX systems by excluding incompatible parts of this module.

* 2022-01-08
	* Fixed: Class `ImplementationError`

* 2022-01-15
	* Added: more arguments for killProcesses()

* 2022-01-25:
	* Adapted: making `netifaces` optional

* 2022-02-06:
	* Improved `ChModValue`

* 2022-08-08:
	* Removed: Dependency to `sh`
	* Removed: `ping()` for Windows (because this functionality is not supported by Windows)

* 2023-06-04:
	* Fixed: Compensated summer time/winter time change in class `D`

* 2024-11-29:
	* Refactoring
	* Improved: Added __bool__ to T1 and T5
	* Migrated to pyproject.toml

* 2025-03-08:
	* Added: `secondsToDHMS()`, `secondsToDHMSf()`, `secondsToYMWDHMSf()`
	* Added: `DurationMeter`

