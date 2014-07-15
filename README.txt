Name: Unbreakable!

Description: Scientist announces unbreakable encryption! The cryptographic
community is bewildered! In a press release, the scientist states that he can
prove that his cryptographic method is theoretically sound. Can you prove
him wrong?

How to Solve: First, XOR all the bytes with the output of the Mersenne Twister
algorithm, seeded with the number '1337' (i.e., in Python). An example of
this is included in src. Next, run strings on the program. There are two
text files embedded within the junk which delimit the location of a flag file.
The file itself is a PNG, which has the flag in it. The other way to find
the flag is by searching the file for the string MCA. A red herring is 
embedded in the comment section of the PNG file.

What to distribute:
dist/challenge - the `encrypted' challenge file

Flag: MCA-F12EE2E5
