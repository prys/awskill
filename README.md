# awskill
Python to destroy resources across all regions.

The idea is to terminate any cost impacting resources across all regions. Should be useful if, for example, your account is compromised and you suddenly see massive instance types appearing in your default VPCs all across the globe.

This is a work in progress and I will annotate properly, add additional resource types and prettify the output as time allows.

PLEASE BE CAREFUL WITH THIS. It will terminate all your EC2 instances across all regions if run as a user with sufficient privileges. I accept no responsibility for any financial loss or any other damages incurred as a result of running this code.
