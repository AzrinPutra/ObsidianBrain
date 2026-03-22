---
title: CSIT123 Computing and Cyber Security Fundamentals
path: "SIM-UOW / CSIT123 Computing and Cyber Security Fundamentals"
url: https://www.notion.so/CSIT123-Computing-and-Cyber-Security-Fundamentals-220bd926b4e4805e8dcfd21c9075268c
created_by: Azrin Putra
last_edited_by: Azrin Putra
last_edited_time: 2025-12-13T12:58:00.000Z
---

# CSIT123 Computing and Cyber Security Fundamentals

#### Bits
- Two Conditions 0/1
- The presence of current flow is represented as 1 and the absence of as
0. This is called a bit, short for binary digit.

#### Operations:Arithmetic
- Addition
ie. X + Y
- Subtraction
ie. X - Y 
= X + (-Y)
- Sign Extension
The first bit determines the sign in 2’s complement
0110 6 1010 -6
00000110 6 11111010 -6

#### Overflow
- In **binary addition**, it's totally normal for the *raw result* to produce more bits than the operands — **because of carry-out**.
```plain text
 1110  (4-bit, −2)
+0111  (4-bit, +7)
-----
10101  (5 bits, due to carry-out)
```
- But in **2’s complement arithmetic**, we **always constrain the result to the same bit-width** (e.g. 4 bits). The **carry-out from the MSB is ignored**.
- Important Rule in 2’s Complement Arithmetic:
Overflow is NOT detected by a carry-out.
It's detected **only when the sign bit behaves incorrectly**, i.e., the result’s sign **does not make sense** for the two inputs.
![Screenshot_2025-07-09_at_11.46.54_AM.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/64e10e6c-af9d-4921-b1e8-2ada19725a23/699415c7-8cc7-4c24-bbfb-bfc15c2d1ba8/Screenshot_2025-07-09_at_11.46.54_AM.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FZYZ23W%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T085335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF65Z3mIijf9dpF4wzBRTglfcbcjXFcns%2BBQ7sQFGHtsAiBmoJjXWNlNbjxnhi0W5VaB6tJtluFc28o9azbGQvlcRSr%2FAwhfEAAaDDYzNzQyMzE4MzgwNSIMFq9iIRSW%2BY3KBALHKtwDD8J3stIlRRpNfW98Iw1HNoo7xY6KSQ9hkzsuYLDbUMsK7ifUhNlnLOExwKzzuMdzx70q0575EfjuKE%2BuvhgTwBLcQVnN3np02ZtH88PpMwMXLlIHxPBf6dufDBXKt17AvtlOmmsT4TbXMxg4pF%2F670KiraTAdWqr5FSyviR%2FVgMMgfap%2FT7CYhKeM5oqrPZu%2Bv73OHWLLb%2Fk6%2BXy1ZrBkZQJh3%2BVcJVBi9wQrImdSzwrCywVaHDXECxOedKH6EmKG6u667Ay5xIle0FaU1yWXaJV9mDMD8QgyPdXl9S54eN0ASkDEIMFYx372C%2FOXTnM2KQ26weACHSWanc%2BGk9aOJ%2FL5GCy2PuTSeLaBGn29IyXcZrPcqwQXEnW%2Bkb2gBBV9hS1cyHqP3t5zOwgDWHEytL0G21yvojYRZkOGRxvjO02NT0Ti5Inis3ibCIDAcuV6MJQOXNH%2F0h34bYF6wY%2Fa%2FG7%2F%2FwWUjYaOG%2B1do2RRdXiYphY8WxUcQ8xCQ9bQPcN9ihUDnOFTe885kc0O5vlTyKxrjESzIxSXH8LwV%2FqpBhE8pPKE4nOpkERBWlZ%2BroGs2nb1ykNJj3jtoYKtWPqR0%2BXcecfw67SDX3Y90h262ICOLUUV12kShFBEK0w6Ij%2BzQY6pgE1EyHdGzIu8b36mL1HHM46jAyPZXbf%2FlEgheDtbxq2o5QaxmKkx2LWsUKwI5KU%2FfiMvlAPAY%2FK%2B6635guQUTBTfyAYhMyBRpi9T575LFSBrnkw9JjkQlBlSv76W1gMKLsms%2FkzEXa7dHscqAE4WP3o1PnBg%2FVhgcIdXF99BMD2GmgYXBd0amdn8MBan1NSJyaBewDD%2BOrxAEQOpU%2B%2B2NpROvB68Ecn&X-Amz-Signature=234e12c8a0be1a22e0547edfd5bdec1607e1b2a649b84aef93b03ee7e6a08225&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

OR the expected result is different from the binary result
![Screenshot_2025-07-09_at_11.47.09_AM.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/64e10e6c-af9d-4921-b1e8-2ada19725a23/0a518acd-b62f-49ee-92b2-2c21aebb930d/Screenshot_2025-07-09_at_11.47.09_AM.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FZYZ23W%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T085335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF65Z3mIijf9dpF4wzBRTglfcbcjXFcns%2BBQ7sQFGHtsAiBmoJjXWNlNbjxnhi0W5VaB6tJtluFc28o9azbGQvlcRSr%2FAwhfEAAaDDYzNzQyMzE4MzgwNSIMFq9iIRSW%2BY3KBALHKtwDD8J3stIlRRpNfW98Iw1HNoo7xY6KSQ9hkzsuYLDbUMsK7ifUhNlnLOExwKzzuMdzx70q0575EfjuKE%2BuvhgTwBLcQVnN3np02ZtH88PpMwMXLlIHxPBf6dufDBXKt17AvtlOmmsT4TbXMxg4pF%2F670KiraTAdWqr5FSyviR%2FVgMMgfap%2FT7CYhKeM5oqrPZu%2Bv73OHWLLb%2Fk6%2BXy1ZrBkZQJh3%2BVcJVBi9wQrImdSzwrCywVaHDXECxOedKH6EmKG6u667Ay5xIle0FaU1yWXaJV9mDMD8QgyPdXl9S54eN0ASkDEIMFYx372C%2FOXTnM2KQ26weACHSWanc%2BGk9aOJ%2FL5GCy2PuTSeLaBGn29IyXcZrPcqwQXEnW%2Bkb2gBBV9hS1cyHqP3t5zOwgDWHEytL0G21yvojYRZkOGRxvjO02NT0Ti5Inis3ibCIDAcuV6MJQOXNH%2F0h34bYF6wY%2Fa%2FG7%2F%2FwWUjYaOG%2B1do2RRdXiYphY8WxUcQ8xCQ9bQPcN9ihUDnOFTe885kc0O5vlTyKxrjESzIxSXH8LwV%2FqpBhE8pPKE4nOpkERBWlZ%2BroGs2nb1ykNJj3jtoYKtWPqR0%2BXcecfw67SDX3Y90h262ICOLUUV12kShFBEK0w6Ij%2BzQY6pgE1EyHdGzIu8b36mL1HHM46jAyPZXbf%2FlEgheDtbxq2o5QaxmKkx2LWsUKwI5KU%2FfiMvlAPAY%2FK%2B6635guQUTBTfyAYhMyBRpi9T575LFSBrnkw9JjkQlBlSv76W1gMKLsms%2FkzEXa7dHscqAE4WP3o1PnBg%2FVhgcIdXF99BMD2GmgYXBd0amdn8MBan1NSJyaBewDD%2BOrxAEQOpU%2B%2B2NpROvB68Ecn&X-Amz-Signature=6d6eba15c3630b67a9f6b3b887378dbbf75e5c565ade2503d2a263d333797ab9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


#### Logic Gates and Truth Table
![Screenshot_2025-07-01_at_10.59.03_AM.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/64e10e6c-af9d-4921-b1e8-2ada19725a23/00004ef6-2d8a-48c1-905f-291bdcec4b6f/Screenshot_2025-07-01_at_10.59.03_AM.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CEEUY6I%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T085335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDT%2FXZy%2FqJr0iKm%2B51iIeJv1X1YEs6tQdz4LoysW10%2FCAiEA8sct9CFv7MIQN3c1cydztlGJ%2B4mj%2Fc%2BRkeTsAPtg7ucq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDKY7HWSYJzEBtqAzJCrcA4dlM4cpmjsB%2FA%2FUkk3j6rvu9vDzF96t44nYv1PLCLYISvUruV6sGhE3B8kSa4pr81%2FHy%2F1aJLYeGx%2B4TGWp2sRw6cfN2TkmAgYFzzb05dDN1bm8qOx1vcAiDAlXroYawi7R9hNoa%2B0Sq%2Fzi9%2FUabNWSj7owxE%2BJH1UulN%2FSdcorIRiix2nCFniHbNkwfGuzqchOvfFF9CqMDKJn9DQt%2Fxv3FBlkzvBcCp6W7AzTOWXrGnmKnI8xa2Cpog0c9UbZU1Jb0kTLxwXyWpyPn5uuam8kJMG1%2B2poyRwam0TNCf3%2FOc9Tzi1dM0bIWJo6JxQ0vBY%2BoWiJ9CLfZ59xkWcahWC8CVXD9di7jyt3X6K439XA3Z3HdxS1tRQGcszTUKHbyQ4W%2BnIE7PMVK5JvmuVjpqbSn%2Bx3OjJ5M0Fg%2F0SO5q%2B%2FLHYeZJes%2BA4P76frOmk947spvNE3l9ddstn4wZBtv5gYvK4csiXMupR9Th9yfkaZYvCm1u9yeLoJ%2B6hkDEegHgLzgAk4iXe7Z4aKlOZ8GBBo7YKt688OZ0ZT0pFFavcEWradK3Huu3BahB7TSXWVePqLkct0aaANqwfgwQ3bAg9Qz6PoLrOFRSJZsEbV7BATnc%2FbXipnDnvt3aABMLqJ%2Fs0GOqUBRIbocNFgT0qZlG8abHMGPZ%2Bczofh4lfdr0lQs4OWBSpxxYcQiqGwXXTDuIDcsaaAhxCe5eYdRfD%2FVKHXSqTbR2ACvEggTLjh6G4hYVniFTlTgn1IhEufcWYifhStzvzjFhD%2FM%2ByKxIIAhol07FHO56peYHTqN%2FN40X2HBNlY6qF6YIt%2BbY1CvtikSZxTujpEuPKLsgwcP5BNTQfh79fk24N3OHMb&X-Amz-Signature=d50d635359b881350c43b6ef2a62d9e057dea9cba98dfc8551e20f42286b05e7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- DeMorgan’s Law
![Screenshot_2025-07-01_at_11.01.34_AM.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/64e10e6c-af9d-4921-b1e8-2ada19725a23/c565c73f-9347-4331-8408-dc392b02edfc/Screenshot_2025-07-01_at_11.01.34_AM.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQR26DPK%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T085335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjhKUZrugjEAWvbYFCciJZX5rXVsBosm8Sj1aIHk3wMAIgD7P2XSUL6%2Bwqf2QNR6XiFmOLB3ZuKartFxy7rMnjEDwq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDEjUzKiqIELH0ERZwircA9pjnwg0MlowYuHkpjB0TNPhfQNMNrJibTbrEP7RKUeAx8wDuIoxcqHULXmSMM%2BAJOMhJo3b02UA6odw%2FE3lBcVINszw9t83IeEtVw5sgLQ%2Fl%2BemicqfA86dKSsVMJihHy3V831OP7DZbToLbnhua8Yp3qbrnT8AHgv%2BdDsTgqujbvgX%2FwL3pfctcrxKI88DIZjnHiEELFg2x4E4ujrhphPJYgp%2BTAUBH3%2Bqs1t2aBQ8f7KWI3jFHteuRz5QWFrd1238vZMJtn2Auh8x1owD76D02pfYpwm54d%2B68QuI1POviqqsPrTQpCVGK3Gcvok%2Fp1qyBoiGnTaUppnl5lf2mRedoykdu9%2FyLc8Wf0%2BUC%2F1994UcyUWxatN2jjEQxVAAgqZxnHrklwhHMKSyIE070%2BpvDyF%2FIho%2FXc%2Bza%2FOAqtmYUDkUwiq2E3dBvrwEtO6wYv7nbkrn4%2BwuW0NnVDW3UgpbzZpZcKlsysgBU1aegRG4x23ORF0D3vfi92Ji2jpuOcxzWvWqOSr4cjtSsLKLxT%2FD5h293UUdQJfD3Xi%2FJVWBynYG68D%2Bo0BH3wgixBFL%2F9lZFAhv3DQINy%2Fx%2FMNS2gBZNPDbrd6jKAmq2PBuvIX7FZKuYC0sxte5Y4giMLuI%2Fs0GOqUBZmrTZegAkPkh3yIBxUMCzy4ZGJzN%2F18vClNHlZq35dStVvko2I2V0Ud5NOPn4CdJUzQC1nJCN%2Fr0m4KO%2BySs4rDIpTMmwsmKL0emRC1GH5Oj8PHhtxdczsASKzjjadAa8wkyCg13lq8wceH5xJJw5CZ9nOfvxh%2BRF%2F3bRQvqulcfCKWiUIE%2BY5dzSZMnE%2B0QO5Exs%2FCR7gTiX66gF2eQ%2Fdgfos1x&X-Amz-Signature=7fd138eca2b191d815faccc7f37a3e69d0fa6b5a42c50390206753baf14b8848&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Need TO KNOW HOW TO OUTPUT THE TRUTH TABLE FROM THE LOGIC GATE