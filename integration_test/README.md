### Integration Testing

This directory is focused on implementing integration testing. 
The naming scheme for these tests should be following the when/given/then pattern
for test function names to provide as much detail as possible.


Please note that these tests may modify the database and should never be run 
on ANY shared environments. If you do run these docker images pointing to a shared
environment you will need to slowly walk each tests output and undo the database entries.