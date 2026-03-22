---
title: Creating HomeLab with Proxmox
path: "Creating HomeLab with Proxmox"
url: https://www.notion.so/Creating-HomeLab-with-Proxmox-13dbd926b4e480d7a338f4768827b96d
created_by: Azrin Putra
last_edited_by: Azrin Putra
last_edited_time: 2025-01-22T05:02:00.000Z
---

# Creating HomeLab with Proxmox


## Homelab w/Proxmox
**Created by:**  Azrin Putra
**Created: 13/11/2024**







### Tools:
1  x PC or Mini PC or equivalent
1 x USB media for os installation
Patience






#### 1. Preparation
- Download Promox VE
	1. Go to [https://www.proxmox.com/en/proxmox-virtual-environment/overview](https://www.proxmox.com/en/proxmox-virtual-environment/overview) and click on Download
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/64e10e6c-af9d-4921-b1e8-2ada19725a23/db322e1b-d7c2-40ed-9603-acaf6360b294/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJJO43KG%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T090108Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBdacd%2FYXtfgqK7dPXQ99IEV62XAU7sBkZP8loBH%2BKl9AiA8d4k8I3LOfRA0HTffNXq0hiPWu9Ie7bKylHes4cE9nCr%2FAwhfEAAaDDYzNzQyMzE4MzgwNSIMa4GH1mrJPeSLvTbFKtwDN3lN2ReWIu73Uyet83tsNLC03ohyXdn9ppw8fRc3aEIdvmER%2B8SY2jwTnirvRToR%2F%2FpckzCbe4LtHpswMZ6aqtDBBVBBxHMxWPIGU7BuK3%2BF8butiKrmWxm5vK5%2By%2B9xfWEu0XaPKdhyI52fid2b5ZSNXJYxkEIcRtHdK5pDZsEiXmZy%2FaJfS%2BX5YZD8JUbhmEQsSLtWSs0Ktb4Hb%2B1qw3DhX2TE5CWhF32PMy%2BTgyawVz9X3TuJBjMmdD%2F7Zks6zIbJPDJtYlmz7kdrI3MZZiyRQ8Uk0iecslzpsxeFA3XkE8KkPsp2tC0OKIKnvuzF4EZxoRJBgxG7PJi4rD6EJVMttyD1xEQSlLaWLMP%2FAT%2Bo%2FjsAK5Asjsle82kPo2vTtskGQxT7O5hPJPR3IauWAXLe7CJMdVRXLIyPOSaP6ue%2Bk%2FK0STWR%2BHtAfqeJYTPyzLbU7BDgr41P8w3VIztax1rABDavcGT%2B7KSmBqwtRbh%2FuJTup%2BtBSUc%2BojYEPxfBE6V9mMY%2BBWxzitJn3PPAC8o3R%2BHyzTH1vDSdOR6LRPQRN7jnYYppJTtxA3f75METZEIPXq1zcJFsMm8TepomND8ucFHczR79C6ctob%2FxmC5mSezZf7%2FiEUWT79AwyIj%2BzQY6pgG0OYMSJcgJgA8HGp%2FUN87zk0do%2BvGbaGd8GnVcfLAB8HRT3VlqBa88e4aAHyb0apNXhgS59DXjmUarqftjPnFTqXcrv3F7HqBF5So2y2buug3JOppXR22pIzOGV8ciwnDwFQ5zKUFQXb5ZFATQjL4jXHBpdigoXXzr0at23KndY07XMJLAvOsN6zbCHvt5b5fQL4PBP%2FWNhW9x8RvG2zijPFpu%2BWva&X-Amz-Signature=21165a8d7746be7485f52794f79f3819393f429bda225278bb6471e3a15af1e5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

	2. Click on Download under Proxmox VE iso installer
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/64e10e6c-af9d-4921-b1e8-2ada19725a23/faa009ce-6882-43e7-b15f-8cbdcc6b636f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJJO43KG%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T090108Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBdacd%2FYXtfgqK7dPXQ99IEV62XAU7sBkZP8loBH%2BKl9AiA8d4k8I3LOfRA0HTffNXq0hiPWu9Ie7bKylHes4cE9nCr%2FAwhfEAAaDDYzNzQyMzE4MzgwNSIMa4GH1mrJPeSLvTbFKtwDN3lN2ReWIu73Uyet83tsNLC03ohyXdn9ppw8fRc3aEIdvmER%2B8SY2jwTnirvRToR%2F%2FpckzCbe4LtHpswMZ6aqtDBBVBBxHMxWPIGU7BuK3%2BF8butiKrmWxm5vK5%2By%2B9xfWEu0XaPKdhyI52fid2b5ZSNXJYxkEIcRtHdK5pDZsEiXmZy%2FaJfS%2BX5YZD8JUbhmEQsSLtWSs0Ktb4Hb%2B1qw3DhX2TE5CWhF32PMy%2BTgyawVz9X3TuJBjMmdD%2F7Zks6zIbJPDJtYlmz7kdrI3MZZiyRQ8Uk0iecslzpsxeFA3XkE8KkPsp2tC0OKIKnvuzF4EZxoRJBgxG7PJi4rD6EJVMttyD1xEQSlLaWLMP%2FAT%2Bo%2FjsAK5Asjsle82kPo2vTtskGQxT7O5hPJPR3IauWAXLe7CJMdVRXLIyPOSaP6ue%2Bk%2FK0STWR%2BHtAfqeJYTPyzLbU7BDgr41P8w3VIztax1rABDavcGT%2B7KSmBqwtRbh%2FuJTup%2BtBSUc%2BojYEPxfBE6V9mMY%2BBWxzitJn3PPAC8o3R%2BHyzTH1vDSdOR6LRPQRN7jnYYppJTtxA3f75METZEIPXq1zcJFsMm8TepomND8ucFHczR79C6ctob%2FxmC5mSezZf7%2FiEUWT79AwyIj%2BzQY6pgG0OYMSJcgJgA8HGp%2FUN87zk0do%2BvGbaGd8GnVcfLAB8HRT3VlqBa88e4aAHyb0apNXhgS59DXjmUarqftjPnFTqXcrv3F7HqBF5So2y2buug3JOppXR22pIzOGV8ciwnDwFQ5zKUFQXb5ZFATQjL4jXHBpdigoXXzr0at23KndY07XMJLAvOsN6zbCHvt5b5fQL4PBP%2FWNhW9x8RvG2zijPFpu%2BWva&X-Amz-Signature=4ce1bc7bcc830f64996ff2f4a082fe4b17c97a57c97e8800a21ba2c9ad01873b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- Download Usbimager for creating our bootable media and load our Promox iso file
	1. Go to  and click on GDI to download
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/64e10e6c-af9d-4921-b1e8-2ada19725a23/b72a4975-02cb-4139-a748-9e66a8bd5387/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ZYC4C3F%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T090107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCciXTEEHHhHOxihQgUB9sNM7a2wInUqB4Hydgb5AhWvQIgbbyZ6QsBxLBqX7Ar5GveLqZTmHh52r5NIdfMM41NWukq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDIdLgMQEP3LwjkNpPSrcA1o3OMtUKBr1gHDssNES3Jd7MIEU8sVLNi06DChN%2F8PX%2BT1OYUi%2BUIjWyO5bpUIc9QFLR3fRR0020r99pFUULcRrz%2FBb%2FRn1r6gedJ93KsVQziRgCfpBDd1xgSGYClrnBH14apVELfTAG4Xz%2B1%2Bhfw5xVIrwTQuziVHOeMO4z8CLfVungJmlqsNfDqf6Fl1ZCiUsdXVpQZL%2FC1dvS5UjT%2FQmB46BlW%2Fd73CgZfYzkmP8JdEsLkyoShOkVBr2U%2FNrj0iqSW1UW3JDux%2BJWeki1W9bb%2F12L1pTwODDjn51U1c%2FNJZ%2B7Ur8AbeYr2YgG79T7OWgo%2BR4gb11AtW3eEuyMNulLYia6%2BpX1oGrYRgoZgZrwGwWWmVP81iyJdCXq8Ha8Tebf2mugr6u2xhjOBCcAehfRZJHG6T4leWCSdnr9ebRDGtWJsmA3QFXIG4nhHSbnpRS4enrljCl8Phn3Zy9BWibUq0oJlcjZ1oTU8erO29PRe0LfnU47sMzb6Tywtyf%2F7k1ARcZkqTdZ%2FijMaiZjDFkM%2FS75v6tW5SKZHAisvFtPArSVSYXoOfUNZodlf7APLbmj7PPxSDxbGVSPcGbIs3AAb6SJZnraq2pxjlCKDEW2uuo5J%2FANCFBh%2FBsMKuJ%2Fs0GOqUBfCO9DCv%2F11LIbGE%2Fl41UJRaSD395%2BROt0vq4EG6gc4p8ypm4KCTsTloP%2F2fLJaNR3j4PnmkD3RNSK5Cdte3EVp708vjmeYCXL%2FzkrU%2F3VsomaojCpPay%2BJbyBv8V0sVH5n02uLkm09CeZyZE2gCnnE8%2BMlXCr35Yj9kVp%2FVRHTaXzEsaUucFmLznX8zWYiDMSTTYtTwE3AoPv9mvyx%2FKmRxGyYxq&X-Amz-Signature=726a48c59312fcc46bcbb05ace7f72571615a4b2f613fc89556068c269d97ff2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
	2. Once we extract and run it, we should see this
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/64e10e6c-af9d-4921-b1e8-2ada19725a23/b1c76564-82d6-4168-ba76-0c49992cb86c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667O5RUYLH%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T090107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6TsMNbRloBbhW0Bc0hX%2BSabPSwtddK767vId7CpGg3QIgf9Tn7RpdtXR3SbirELd20UzmjIq%2BIwZA7Veg6lII2BAq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDBD0b0WmGsSjlxJAKCrcA5QD%2BF2gwObYGqcRUeCXJDv94i2T6H35ECO06M51EETXlHoPtDy%2FOIpim38S0CKV1cS19yi8HYiVe2K0PNx%2BfMs9%2FMplwsgokZr7cA3cejIz7PUc%2FjoB9hEMwPVrlEEZgJVDwb6jrO0XBToJf1Ku6TAa20gEMvkwxFeULL%2FlY%2BiF7FyYH6BEK3TkS%2FxmDqjf1oq5GLEhyFTBP0DWx2nQCczDE0mjzr3q4gCCdoiQvm9acY62ARR3Kwj1GmjlVqmmaCBDOsGPXtWn54tOnbwKP%2FRrqAhI7LnbLP4UYJED7Fj6rNORWhqFjLIr%2BO4XB%2BKeBwwUBWoAXbtzBKKrQAVEQ3c3lZyj%2FVrCBwBYovwY7KvQJNbsfkxIl1h3OW49BM%2FUvBvPmBcXKAGKKesegV%2Bjs%2F6aHYhtUtyI%2BDGee4K5G%2BY5iC6ckTpjJNJyYl%2BKjtyw2kuVrku5MvhQLQIhfj8xOOyfuO50I2AhBTHxQT4FVtvmJUsiEOT6ww18cKV7tNvs49sGUx4p2Eqie%2FzvXBs8Bo5kp2B8vkKl1d8AiLupV5Cql5Ew2FA5o%2Ff%2B2KJQDnJXxRWCVyGstDhgVkofEIEERdepxgjf9ZG9sZX%2F7OCTGmAadwunQRxz6gyupe2lMMiI%2Fs0GOqUBcpz%2BmGy77iE0KO9lhGLOM5SHspU%2Fr7%2B%2FworlVF6CLNVNsDgiZkQLfCQRNDlGSnJ5axthHNQLw9YXAF2yx4MjwsD3YwQJKm%2BMe99lFR9FqLwR2Oc71jbKkBNy7SSfLGLsCzw3T3JAt4HyX12KZsS%2F8KeQ1d2ADM%2FQLeGPOrZ7AZ%2BBbcngKGOwgwRmu06g1EJvnUcKiDboX%2FOtaH1Zce0Mi2EjxGAz&X-Amz-Signature=87594aebb4cc045c9ba1988ca53ec9e769371676dd8965aa681a14c1a7dd7491&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

	3. Select the iso file for Promox via the three dots icon and also the target usb media
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/64e10e6c-af9d-4921-b1e8-2ada19725a23/96dd545f-1b15-4700-883a-8ca78297133a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667O5RUYLH%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T090107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6TsMNbRloBbhW0Bc0hX%2BSabPSwtddK767vId7CpGg3QIgf9Tn7RpdtXR3SbirELd20UzmjIq%2BIwZA7Veg6lII2BAq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDBD0b0WmGsSjlxJAKCrcA5QD%2BF2gwObYGqcRUeCXJDv94i2T6H35ECO06M51EETXlHoPtDy%2FOIpim38S0CKV1cS19yi8HYiVe2K0PNx%2BfMs9%2FMplwsgokZr7cA3cejIz7PUc%2FjoB9hEMwPVrlEEZgJVDwb6jrO0XBToJf1Ku6TAa20gEMvkwxFeULL%2FlY%2BiF7FyYH6BEK3TkS%2FxmDqjf1oq5GLEhyFTBP0DWx2nQCczDE0mjzr3q4gCCdoiQvm9acY62ARR3Kwj1GmjlVqmmaCBDOsGPXtWn54tOnbwKP%2FRrqAhI7LnbLP4UYJED7Fj6rNORWhqFjLIr%2BO4XB%2BKeBwwUBWoAXbtzBKKrQAVEQ3c3lZyj%2FVrCBwBYovwY7KvQJNbsfkxIl1h3OW49BM%2FUvBvPmBcXKAGKKesegV%2Bjs%2F6aHYhtUtyI%2BDGee4K5G%2BY5iC6ckTpjJNJyYl%2BKjtyw2kuVrku5MvhQLQIhfj8xOOyfuO50I2AhBTHxQT4FVtvmJUsiEOT6ww18cKV7tNvs49sGUx4p2Eqie%2FzvXBs8Bo5kp2B8vkKl1d8AiLupV5Cql5Ew2FA5o%2Ff%2B2KJQDnJXxRWCVyGstDhgVkofEIEERdepxgjf9ZG9sZX%2F7OCTGmAadwunQRxz6gyupe2lMMiI%2Fs0GOqUBcpz%2BmGy77iE0KO9lhGLOM5SHspU%2Fr7%2B%2FworlVF6CLNVNsDgiZkQLfCQRNDlGSnJ5axthHNQLw9YXAF2yx4MjwsD3YwQJKm%2BMe99lFR9FqLwR2Oc71jbKkBNy7SSfLGLsCzw3T3JAt4HyX12KZsS%2F8KeQ1d2ADM%2FQLeGPOrZ7AZ%2BBbcngKGOwgwRmu06g1EJvnUcKiDboX%2FOtaH1Zce0Mi2EjxGAz&X-Amz-Signature=9290ae09d55f7468c8cb990085bd0a429185416147f3512e819a17e775335720&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Click Write to execute the process.

	4. Once successful, we will see this
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/64e10e6c-af9d-4921-b1e8-2ada19725a23/534115b7-7a2f-4af5-bd82-81e67b4d69fc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667O5RUYLH%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T090107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6TsMNbRloBbhW0Bc0hX%2BSabPSwtddK767vId7CpGg3QIgf9Tn7RpdtXR3SbirELd20UzmjIq%2BIwZA7Veg6lII2BAq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDBD0b0WmGsSjlxJAKCrcA5QD%2BF2gwObYGqcRUeCXJDv94i2T6H35ECO06M51EETXlHoPtDy%2FOIpim38S0CKV1cS19yi8HYiVe2K0PNx%2BfMs9%2FMplwsgokZr7cA3cejIz7PUc%2FjoB9hEMwPVrlEEZgJVDwb6jrO0XBToJf1Ku6TAa20gEMvkwxFeULL%2FlY%2BiF7FyYH6BEK3TkS%2FxmDqjf1oq5GLEhyFTBP0DWx2nQCczDE0mjzr3q4gCCdoiQvm9acY62ARR3Kwj1GmjlVqmmaCBDOsGPXtWn54tOnbwKP%2FRrqAhI7LnbLP4UYJED7Fj6rNORWhqFjLIr%2BO4XB%2BKeBwwUBWoAXbtzBKKrQAVEQ3c3lZyj%2FVrCBwBYovwY7KvQJNbsfkxIl1h3OW49BM%2FUvBvPmBcXKAGKKesegV%2Bjs%2F6aHYhtUtyI%2BDGee4K5G%2BY5iC6ckTpjJNJyYl%2BKjtyw2kuVrku5MvhQLQIhfj8xOOyfuO50I2AhBTHxQT4FVtvmJUsiEOT6ww18cKV7tNvs49sGUx4p2Eqie%2FzvXBs8Bo5kp2B8vkKl1d8AiLupV5Cql5Ew2FA5o%2Ff%2B2KJQDnJXxRWCVyGstDhgVkofEIEERdepxgjf9ZG9sZX%2F7OCTGmAadwunQRxz6gyupe2lMMiI%2Fs0GOqUBcpz%2BmGy77iE0KO9lhGLOM5SHspU%2Fr7%2B%2FworlVF6CLNVNsDgiZkQLfCQRNDlGSnJ5axthHNQLw9YXAF2yx4MjwsD3YwQJKm%2BMe99lFR9FqLwR2Oc71jbKkBNy7SSfLGLsCzw3T3JAt4HyX12KZsS%2F8KeQ1d2ADM%2FQLeGPOrZ7AZ%2BBbcngKGOwgwRmu06g1EJvnUcKiDboX%2FOtaH1Zce0Mi2EjxGAz&X-Amz-Signature=377a2f70107e9bcf668ec5dfaac8a4d75df4ed91aac495d48da0c20d827e0cb9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


#### 2. Installing Promox
- 
1. 
2. 
3. 
4. 

#### 3. Accessing Promox through WebUI
- Setting up Promox for the first time
	1. Go to your main machine and access Proxmox thru your web browser via <yourproxmoxip:8006>
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/64e10e6c-af9d-4921-b1e8-2ada19725a23/d1aa1e65-f8ec-4a83-bf3a-71ed261e0338/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UCMLHBJ%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T090107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF5oR9WrJm00xMc2buFEj4s0k3q1RKh1Vd%2B1v2%2FSdO7jAiEApqTHC%2Fsqk%2FO0CZwb5OiY2kY7AlkBiX5Vhsg32NJ3husq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDIwd3T%2BPQ0FeYXZgfSrcA1Hu1O8UFgKmeTiq5CfcJxb0OAFVFK3yL6GBMhmb370D6LMdE3bJ4Nllffp6ICIlzeFhDscZvqYsXDPRPJmWi1HuMkX91rz4m1lHB68tFjjrSa4nQBRhAzWeClp7wtKuL47aWbn6FK5GmirY5fjjBr1xwi6stuUhitm911XYBqIpBgoWwyWByT3Tx%2FieXTNI8PIfmDHaeVpq9rmw80Pu8U0%2BrUE2%2Bp9WRHcFMlQ0O4ucMJX8m8eNnOOIN%2Bx44S3HFSXkeMH4Flvo6%2Far5GIHiPsS%2BkRcyZ5bytcq8OIlG8ZWIbmkMK6X3bXHGFpjzieF5jWjzQ%2BtQAtr9dt8%2BcsSfDvRKyps18ykKEMCqq4PCBRVldwwKAwenr9XEWs8sFWnsD5kThq9AMIm4WD%2FtaubuExJhAWtcHildR5FqKJdTuLjqlzZ4hYsz%2FfOjiBvh6NSzb7U8prcSfQLyHJVFBvknJLGWuf2DaoMOTElfoHf%2BMHHRO1ujZKKuflpsxRWHo6g3ZRKV15jju8K0yVUu%2FlnvTE9tnDAi2AgkIIEHSEcprlEynKQISFsBbQclz1uPSyux4wDwDRLKItpctUsoe9k3PlV3uZcKl%2F5AM3jw%2BGOxVmneS4FrYPDqg0CrfB6MJ2J%2Fs0GOqUBbLokCk8%2FYIGm3FO88MlHxDaq9cFm7uYp30wjJIYqs%2FTHC70QPQlTkwOxonjoKpuM7RME%2FJD%2F%2Bo%2FidnAHGF4eah0YHDyG154O8eKZutpZydttfZecn4W3kAO9Qhx2q1N8kJ3lZ3%2FzkjZpSDu5ypQnY%2FVJ9sJomxvzcOix3o2MV4aB%2FHxgnqUFZGW%2BfAJ7j4022%2Bz6K7VnSSWiLIevyZdiIo%2B%2B25EQ&X-Amz-Signature=7b8e832c6a75450ed043146080c1d491a2897b799b54db5781204e38be2592c6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

	2. After logging in, we will need to update Proxmox so we can click on our only node i.e. theblackhole for mine
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/64e10e6c-af9d-4921-b1e8-2ada19725a23/cb9af09f-5b4b-4d79-be7c-797530522853/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UCMLHBJ%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T090107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF5oR9WrJm00xMc2buFEj4s0k3q1RKh1Vd%2B1v2%2FSdO7jAiEApqTHC%2Fsqk%2FO0CZwb5OiY2kY7AlkBiX5Vhsg32NJ3husq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDIwd3T%2BPQ0FeYXZgfSrcA1Hu1O8UFgKmeTiq5CfcJxb0OAFVFK3yL6GBMhmb370D6LMdE3bJ4Nllffp6ICIlzeFhDscZvqYsXDPRPJmWi1HuMkX91rz4m1lHB68tFjjrSa4nQBRhAzWeClp7wtKuL47aWbn6FK5GmirY5fjjBr1xwi6stuUhitm911XYBqIpBgoWwyWByT3Tx%2FieXTNI8PIfmDHaeVpq9rmw80Pu8U0%2BrUE2%2Bp9WRHcFMlQ0O4ucMJX8m8eNnOOIN%2Bx44S3HFSXkeMH4Flvo6%2Far5GIHiPsS%2BkRcyZ5bytcq8OIlG8ZWIbmkMK6X3bXHGFpjzieF5jWjzQ%2BtQAtr9dt8%2BcsSfDvRKyps18ykKEMCqq4PCBRVldwwKAwenr9XEWs8sFWnsD5kThq9AMIm4WD%2FtaubuExJhAWtcHildR5FqKJdTuLjqlzZ4hYsz%2FfOjiBvh6NSzb7U8prcSfQLyHJVFBvknJLGWuf2DaoMOTElfoHf%2BMHHRO1ujZKKuflpsxRWHo6g3ZRKV15jju8K0yVUu%2FlnvTE9tnDAi2AgkIIEHSEcprlEynKQISFsBbQclz1uPSyux4wDwDRLKItpctUsoe9k3PlV3uZcKl%2F5AM3jw%2BGOxVmneS4FrYPDqg0CrfB6MJ2J%2Fs0GOqUBbLokCk8%2FYIGm3FO88MlHxDaq9cFm7uYp30wjJIYqs%2FTHC70QPQlTkwOxonjoKpuM7RME%2FJD%2F%2Bo%2FidnAHGF4eah0YHDyG154O8eKZutpZydttfZecn4W3kAO9Qhx2q1N8kJ3lZ3%2FzkjZpSDu5ypQnY%2FVJ9sJomxvzcOix3o2MV4aB%2FHxgnqUFZGW%2BfAJ7j4022%2Bz6K7VnSSWiLIevyZdiIo%2B%2B25EQ&X-Amz-Signature=5e7b85bfe100e7727ec19c248584543f51d73c1e012ab6c8444e1d925413d3ae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
	3. Click on refresh and we should see some errors as we are on the non-enterprise version
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/64e10e6c-af9d-4921-b1e8-2ada19725a23/4ec39491-7a85-4629-8689-42fb80319362/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UCMLHBJ%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T090107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF5oR9WrJm00xMc2buFEj4s0k3q1RKh1Vd%2B1v2%2FSdO7jAiEApqTHC%2Fsqk%2FO0CZwb5OiY2kY7AlkBiX5Vhsg32NJ3husq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDIwd3T%2BPQ0FeYXZgfSrcA1Hu1O8UFgKmeTiq5CfcJxb0OAFVFK3yL6GBMhmb370D6LMdE3bJ4Nllffp6ICIlzeFhDscZvqYsXDPRPJmWi1HuMkX91rz4m1lHB68tFjjrSa4nQBRhAzWeClp7wtKuL47aWbn6FK5GmirY5fjjBr1xwi6stuUhitm911XYBqIpBgoWwyWByT3Tx%2FieXTNI8PIfmDHaeVpq9rmw80Pu8U0%2BrUE2%2Bp9WRHcFMlQ0O4ucMJX8m8eNnOOIN%2Bx44S3HFSXkeMH4Flvo6%2Far5GIHiPsS%2BkRcyZ5bytcq8OIlG8ZWIbmkMK6X3bXHGFpjzieF5jWjzQ%2BtQAtr9dt8%2BcsSfDvRKyps18ykKEMCqq4PCBRVldwwKAwenr9XEWs8sFWnsD5kThq9AMIm4WD%2FtaubuExJhAWtcHildR5FqKJdTuLjqlzZ4hYsz%2FfOjiBvh6NSzb7U8prcSfQLyHJVFBvknJLGWuf2DaoMOTElfoHf%2BMHHRO1ujZKKuflpsxRWHo6g3ZRKV15jju8K0yVUu%2FlnvTE9tnDAi2AgkIIEHSEcprlEynKQISFsBbQclz1uPSyux4wDwDRLKItpctUsoe9k3PlV3uZcKl%2F5AM3jw%2BGOxVmneS4FrYPDqg0CrfB6MJ2J%2Fs0GOqUBbLokCk8%2FYIGm3FO88MlHxDaq9cFm7uYp30wjJIYqs%2FTHC70QPQlTkwOxonjoKpuM7RME%2FJD%2F%2Bo%2FidnAHGF4eah0YHDyG154O8eKZutpZydttfZecn4W3kAO9Qhx2q1N8kJ3lZ3%2FzkjZpSDu5ypQnY%2FVJ9sJomxvzcOix3o2MV4aB%2FHxgnqUFZGW%2BfAJ7j4022%2Bz6K7VnSSWiLIevyZdiIo%2B%2B25EQ&X-Amz-Signature=739f626c5156b2319f95534e43c0475b95126d48b6fdbc65de218455ee2c2d4f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
	4. We will need to do some tweaks to get it working. We can click on shell and enter the commands below
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/64e10e6c-af9d-4921-b1e8-2ada19725a23/acb61c2d-18e4-4095-9dd5-8bf5d2c674c7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UCMLHBJ%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T090107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF5oR9WrJm00xMc2buFEj4s0k3q1RKh1Vd%2B1v2%2FSdO7jAiEApqTHC%2Fsqk%2FO0CZwb5OiY2kY7AlkBiX5Vhsg32NJ3husq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDIwd3T%2BPQ0FeYXZgfSrcA1Hu1O8UFgKmeTiq5CfcJxb0OAFVFK3yL6GBMhmb370D6LMdE3bJ4Nllffp6ICIlzeFhDscZvqYsXDPRPJmWi1HuMkX91rz4m1lHB68tFjjrSa4nQBRhAzWeClp7wtKuL47aWbn6FK5GmirY5fjjBr1xwi6stuUhitm911XYBqIpBgoWwyWByT3Tx%2FieXTNI8PIfmDHaeVpq9rmw80Pu8U0%2BrUE2%2Bp9WRHcFMlQ0O4ucMJX8m8eNnOOIN%2Bx44S3HFSXkeMH4Flvo6%2Far5GIHiPsS%2BkRcyZ5bytcq8OIlG8ZWIbmkMK6X3bXHGFpjzieF5jWjzQ%2BtQAtr9dt8%2BcsSfDvRKyps18ykKEMCqq4PCBRVldwwKAwenr9XEWs8sFWnsD5kThq9AMIm4WD%2FtaubuExJhAWtcHildR5FqKJdTuLjqlzZ4hYsz%2FfOjiBvh6NSzb7U8prcSfQLyHJVFBvknJLGWuf2DaoMOTElfoHf%2BMHHRO1ujZKKuflpsxRWHo6g3ZRKV15jju8K0yVUu%2FlnvTE9tnDAi2AgkIIEHSEcprlEynKQISFsBbQclz1uPSyux4wDwDRLKItpctUsoe9k3PlV3uZcKl%2F5AM3jw%2BGOxVmneS4FrYPDqg0CrfB6MJ2J%2Fs0GOqUBbLokCk8%2FYIGm3FO88MlHxDaq9cFm7uYp30wjJIYqs%2FTHC70QPQlTkwOxonjoKpuM7RME%2FJD%2F%2Bo%2FidnAHGF4eah0YHDyG154O8eKZutpZydttfZecn4W3kAO9Qhx2q1N8kJ3lZ3%2FzkjZpSDu5ypQnY%2FVJ9sJomxvzcOix3o2MV4aB%2FHxgnqUFZGW%2BfAJ7j4022%2Bz6K7VnSSWiLIevyZdiIo%2B%2B25EQ&X-Amz-Signature=8c234d4e0b51d0299fa6fff1ecbcf10e1fbc0dd629e5d217b9cc3134e7d66656&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
```shell
nano /etc/apt/sources.list.d/pve-enterprise.list
#Comment out the link ending with pve-subscription in this list

nano /etc/apt/sources.list.d/ceph.list
#Comment out this link 'deb https://enterprise.proxmox.com/debian/ceph-quincy bookworm enterpris'

nano /etc/apt/sources.list
#Add this link deb http://download.proxmox.com/debian/pve bookworm pve-no-subscription

#We should be able to run apt-get now
```
	5. Now let’s add the no subscription repository
Click on Repositories
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/64e10e6c-af9d-4921-b1e8-2ada19725a23/dac4ee0c-36d7-41ff-b550-bf7778c1b390/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UCMLHBJ%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T090107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF5oR9WrJm00xMc2buFEj4s0k3q1RKh1Vd%2B1v2%2FSdO7jAiEApqTHC%2Fsqk%2FO0CZwb5OiY2kY7AlkBiX5Vhsg32NJ3husq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDIwd3T%2BPQ0FeYXZgfSrcA1Hu1O8UFgKmeTiq5CfcJxb0OAFVFK3yL6GBMhmb370D6LMdE3bJ4Nllffp6ICIlzeFhDscZvqYsXDPRPJmWi1HuMkX91rz4m1lHB68tFjjrSa4nQBRhAzWeClp7wtKuL47aWbn6FK5GmirY5fjjBr1xwi6stuUhitm911XYBqIpBgoWwyWByT3Tx%2FieXTNI8PIfmDHaeVpq9rmw80Pu8U0%2BrUE2%2Bp9WRHcFMlQ0O4ucMJX8m8eNnOOIN%2Bx44S3HFSXkeMH4Flvo6%2Far5GIHiPsS%2BkRcyZ5bytcq8OIlG8ZWIbmkMK6X3bXHGFpjzieF5jWjzQ%2BtQAtr9dt8%2BcsSfDvRKyps18ykKEMCqq4PCBRVldwwKAwenr9XEWs8sFWnsD5kThq9AMIm4WD%2FtaubuExJhAWtcHildR5FqKJdTuLjqlzZ4hYsz%2FfOjiBvh6NSzb7U8prcSfQLyHJVFBvknJLGWuf2DaoMOTElfoHf%2BMHHRO1ujZKKuflpsxRWHo6g3ZRKV15jju8K0yVUu%2FlnvTE9tnDAi2AgkIIEHSEcprlEynKQISFsBbQclz1uPSyux4wDwDRLKItpctUsoe9k3PlV3uZcKl%2F5AM3jw%2BGOxVmneS4FrYPDqg0CrfB6MJ2J%2Fs0GOqUBbLokCk8%2FYIGm3FO88MlHxDaq9cFm7uYp30wjJIYqs%2FTHC70QPQlTkwOxonjoKpuM7RME%2FJD%2F%2Bo%2FidnAHGF4eah0YHDyG154O8eKZutpZydttfZecn4W3kAO9Qhx2q1N8kJ3lZ3%2FzkjZpSDu5ypQnY%2FVJ9sJomxvzcOix3o2MV4aB%2FHxgnqUFZGW%2BfAJ7j4022%2Bz6K7VnSSWiLIevyZdiIo%2B%2B25EQ&X-Amz-Signature=9cbd5d18f0b776e576a30ab9f3e83ff5de2114c6bebbb38399b2f730b646e038&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Click on Add
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/64e10e6c-af9d-4921-b1e8-2ada19725a23/1950d04d-2423-42c8-8e64-e8b6ba725a40/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UCMLHBJ%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T090107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF5oR9WrJm00xMc2buFEj4s0k3q1RKh1Vd%2B1v2%2FSdO7jAiEApqTHC%2Fsqk%2FO0CZwb5OiY2kY7AlkBiX5Vhsg32NJ3husq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDIwd3T%2BPQ0FeYXZgfSrcA1Hu1O8UFgKmeTiq5CfcJxb0OAFVFK3yL6GBMhmb370D6LMdE3bJ4Nllffp6ICIlzeFhDscZvqYsXDPRPJmWi1HuMkX91rz4m1lHB68tFjjrSa4nQBRhAzWeClp7wtKuL47aWbn6FK5GmirY5fjjBr1xwi6stuUhitm911XYBqIpBgoWwyWByT3Tx%2FieXTNI8PIfmDHaeVpq9rmw80Pu8U0%2BrUE2%2Bp9WRHcFMlQ0O4ucMJX8m8eNnOOIN%2Bx44S3HFSXkeMH4Flvo6%2Far5GIHiPsS%2BkRcyZ5bytcq8OIlG8ZWIbmkMK6X3bXHGFpjzieF5jWjzQ%2BtQAtr9dt8%2BcsSfDvRKyps18ykKEMCqq4PCBRVldwwKAwenr9XEWs8sFWnsD5kThq9AMIm4WD%2FtaubuExJhAWtcHildR5FqKJdTuLjqlzZ4hYsz%2FfOjiBvh6NSzb7U8prcSfQLyHJVFBvknJLGWuf2DaoMOTElfoHf%2BMHHRO1ujZKKuflpsxRWHo6g3ZRKV15jju8K0yVUu%2FlnvTE9tnDAi2AgkIIEHSEcprlEynKQISFsBbQclz1uPSyux4wDwDRLKItpctUsoe9k3PlV3uZcKl%2F5AM3jw%2BGOxVmneS4FrYPDqg0CrfB6MJ2J%2Fs0GOqUBbLokCk8%2FYIGm3FO88MlHxDaq9cFm7uYp30wjJIYqs%2FTHC70QPQlTkwOxonjoKpuM7RME%2FJD%2F%2Bo%2FidnAHGF4eah0YHDyG154O8eKZutpZydttfZecn4W3kAO9Qhx2q1N8kJ3lZ3%2FzkjZpSDu5ypQnY%2FVJ9sJomxvzcOix3o2MV4aB%2FHxgnqUFZGW%2BfAJ7j4022%2Bz6K7VnSSWiLIevyZdiIo%2B%2B25EQ&X-Amz-Signature=2d1c6816c2f7205f226b808f4af64dd653fffe35ae3aeca545f048490eb50297&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
Select the no subscription option and click on Add
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/64e10e6c-af9d-4921-b1e8-2ada19725a23/44ef6e11-2bb5-4962-ab47-3d6277d2e3de/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UCMLHBJ%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T090107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF5oR9WrJm00xMc2buFEj4s0k3q1RKh1Vd%2B1v2%2FSdO7jAiEApqTHC%2Fsqk%2FO0CZwb5OiY2kY7AlkBiX5Vhsg32NJ3husq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDIwd3T%2BPQ0FeYXZgfSrcA1Hu1O8UFgKmeTiq5CfcJxb0OAFVFK3yL6GBMhmb370D6LMdE3bJ4Nllffp6ICIlzeFhDscZvqYsXDPRPJmWi1HuMkX91rz4m1lHB68tFjjrSa4nQBRhAzWeClp7wtKuL47aWbn6FK5GmirY5fjjBr1xwi6stuUhitm911XYBqIpBgoWwyWByT3Tx%2FieXTNI8PIfmDHaeVpq9rmw80Pu8U0%2BrUE2%2Bp9WRHcFMlQ0O4ucMJX8m8eNnOOIN%2Bx44S3HFSXkeMH4Flvo6%2Far5GIHiPsS%2BkRcyZ5bytcq8OIlG8ZWIbmkMK6X3bXHGFpjzieF5jWjzQ%2BtQAtr9dt8%2BcsSfDvRKyps18ykKEMCqq4PCBRVldwwKAwenr9XEWs8sFWnsD5kThq9AMIm4WD%2FtaubuExJhAWtcHildR5FqKJdTuLjqlzZ4hYsz%2FfOjiBvh6NSzb7U8prcSfQLyHJVFBvknJLGWuf2DaoMOTElfoHf%2BMHHRO1ujZKKuflpsxRWHo6g3ZRKV15jju8K0yVUu%2FlnvTE9tnDAi2AgkIIEHSEcprlEynKQISFsBbQclz1uPSyux4wDwDRLKItpctUsoe9k3PlV3uZcKl%2F5AM3jw%2BGOxVmneS4FrYPDqg0CrfB6MJ2J%2Fs0GOqUBbLokCk8%2FYIGm3FO88MlHxDaq9cFm7uYp30wjJIYqs%2FTHC70QPQlTkwOxonjoKpuM7RME%2FJD%2F%2Bo%2FidnAHGF4eah0YHDyG154O8eKZutpZydttfZecn4W3kAO9Qhx2q1N8kJ3lZ3%2FzkjZpSDu5ypQnY%2FVJ9sJomxvzcOix3o2MV4aB%2FHxgnqUFZGW%2BfAJ7j4022%2Bz6K7VnSSWiLIevyZdiIo%2B%2B25EQ&X-Amz-Signature=ebec2da6870fa56eae79954aec7c0be8a1f43ef8bf5732c2650d0010ec0b2762&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
	6. Once done, we can click on Refresh and we can run Updates. Once done, reboot the system
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/64e10e6c-af9d-4921-b1e8-2ada19725a23/f8b66c9f-9236-480d-a453-d6893a8eadb1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5XGRDNW%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T090108Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHtIzl8lu7hUJ3Rcd8Rz54QAfqGHSYkXuKGuX9Q%2FA5HmAiEAuAJyscZlzUS%2F6f6nyag1nMtgRiwVFTV%2F0%2FNfsPUAsEQq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDNLAp6%2Bg83UVRf1x6ircA%2Bhw%2FQMvh4YR0o83my2wSwcP6u176yQQK0p8TQOA4%2FGm0fgI2%2BnvkPltyc6n9Ga8LpNHT9Gr0KLNaXpV2T6K3nTv2EKqY1oYuVTepjrx9Jr8bghk6VPKJkFsjk3KwLLBrWzpIIzyf0eIhFPREGZpwbyGWRjO9cm4RfzQJfzEpSTcYq68Rrb73P9TZA%2BG%2FTj12Tx8JJpU7pjGkGAZy1Q6E1YYeFJ3HBWzLE0VDYxyhnV0U%2FIWzgmLJiDK6KJXqq3THEB4B2prZe933%2FF0AvRZQkOqqt0pjxHk9Y0eKwqoDlRF35N7vDGnUM4uORbWKH%2BS8NienKT3lveDNx2uvD02Sq9TleO3UxExyGdOFPQE4Os%2F%2FskS9BYvMeoYkTHANRZYry9ChDv8Nrer1PV7ZjCBJKADd0tEPrT6A4JT0F2Sse%2FhHg00Wthir04xa9sogxvMPCVNuap2DBvJcNIy0vH3BhxVa5WYDBvuNaIHO2NHtlxA5LDWWr%2FP3ujEMnVGX%2BiRFZqS493ssiI5CULqtMfWF2WXoiDuUdpYtqP%2F%2F%2BnKQY7dbfafhHfjYJc2vnGaH3SRh8Yycha38six8xQd6JHn0L9EW0awVFB25E3GKhNTjuORWAK%2BfrS7N1%2FCCDvgMMuJ%2Fs0GOqUBzQBq%2FTpfzE%2BV6vm%2BPy304CqyvoiytwhH%2FdsJF5ESbU0u13id2%2BoiWYhbupZX57j5hfn6X5rcXCCwfHQhrv3Fh0oPpjsA6D0fb%2B3KdVTK4hLnX%2Bb6iVS6nuENY2pqbLIYtcX8Iyanhy6%2FJMXfiUtdnneIWGnxgl8RM9Cfp4rB7zTm8S%2BOdT1Cwe9wY44r2MJOgiuTKkYhYq8QWBqPSsgZZZCmoL%2Bc&X-Amz-Signature=3d1ca4bde04495b26a74a336fc69500afd56cd681b5fa848a65b0833de3b4b14&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
💡 Bonus tip: Run `lsblk` and remove your bootable usb media with eject /dev/sdX (in my case it was sda)








#### 4. Proxmox Networking Setup

First, we need to create a backup of the current networking setup while in /etc/network/interface
```bash
cat /etc/network/interface > interface.bak
```

This way, if we mess up, we can always restore the original networking setup via
```bash
## while in /etc/network/interface
cat interface.bak > interface
## to reload the networking configuration
ifreload -a
```

Next, we need to install openvswitch dependencies
```bash
apt install ifupdown2 openvswitch-switch -y
```

By default, Proxmox uses Linux bridges but in this homelab usage, it is not suitable as we need more than 1 NIC to create our various network clusters(LAN,DMZ)  
We can now delete the initial Linux bridge (vmbr0) and replace it with OVS bridge vmbr0 instead


![Screenshot_2025-01-17_151614.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/64e10e6c-af9d-4921-b1e8-2ada19725a23/0d319fae-1554-4cb5-8134-5c6174806b3f/Screenshot_2025-01-17_151614.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZKQ67GE3%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T090109Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC2%2BhUx9V5lIUTKuu0Y748YHgemL%2F7FLxdkgHM7eoKcywIhAPbrI2kNZ5eDbfGX2XaPQzIYGNOp11NFEMbn8tigf%2BhwKv8DCF8QABoMNjM3NDIzMTgzODA1Igzb5F1bb1MkbSuWCyoq3ANhxLhTsLfupMfH7v1QEaY80CL8i7oSkLltpemBA82IiRCIQUM3AnvoJBtl1U72zK8ctQIwM8tIZiP923LsdgKvUA72dOMr7hDHPzTRljjxsz%2FhFA850%2FCMYh1VSbTPVR6DMt9xsYzSPVYViyBrY%2B%2BSrhHRijmJxw8SSFe0y8kJ2BDhsdTzqDT%2B1%2Fk3QbjkJlxXw3uz6fruux%2BfvbZrRebnxMKjE2%2BQmcy2gVXu1ORQZPSoFu6PUqXDysrA7%2Fu%2FeOuQyT6uGRZ98qMJONPZ3xcdswCUyH119Xprkk9MX%2BRfbs%2B8ZQppeEaIQ%2BuefwJQnvPQRH8MBdyMpf2XceUyr7LDhrc67caCkNpDbAzcAJnoVIGNCdTsDcDF8E1%2FSxh1%2BAYzlMRAwOj58k%2F2JnBXUYIEwpvumXefN%2BSYKNtHpCncok7Y6JiS0Pmj43ArPKvzyJC%2FQciJedLKogKSScaNIPSyuyyeVSbv0%2BL2zNiEUVg8C5BDzvJtTiJOZmvNpIHmNYnoPfZBzesTPzUGU2TojXnOLz74gwa7nuwLSJ12muYhRin70ttviqkp%2B4MjmjV5b2qJ6K2JvZq8EbnKI%2F9arLoYCg%2Fhvh04RJv1AoQYrhoIFJDnQe37MqjFZcVVQDDJiP7NBjqkAcPHDkN7gSbh0QZSpPAUDj%2BomTd%2Bc4jm7%2BoLrWTNM6a%2BsYO4t%2FvucRw1IXgr2FWlYqXNrhyvj6wgtc%2FNoaC%2BLwnuPK3o6Xcui936a%2FhCXFe%2BqAJ4o3nhKrnMwbSKZzJ5gsbW1zRNE4lxjs1VAtGy3CbXRMR9ufC%2FQjVMKbL%2Fa4KH4LnWUW4Cw5C5OZUnZbyv1pB%2F6JsjS%2BWSD5B1E4hDxqROxQmz&X-Amz-Signature=96291bea086c570a83746d942d462c24301a53c8550f6f1f4d2183a44a5a4b9f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)




We also need to create another OVS IntPort called vmbr0_mgmt. This allows us to maintain our original connection to Proxmox WebUI




#### 5. Enabling copy and paste in Proxmox via noVNC

It's actually pretty easy now.
You can enable the VNC clipboard by setting clipboard to vnc. You DO NOT have to use the Spice console. This works in VNC, just uses Spice driver to...make it easier.
A. (through SSH or command prompt in Linux ) install the *spice-agent* drivers) in the VM.
`sudo apt install spice-vdagent`
B. Enable the VNC clipboard through Proxmox shell/SSD
`qm set <vmid> -vga <displaytype>,clipboard=vnc`
For example, my PopOS VM is 101, and I'm using VirtIO-GPU, so my command would be:
`qm set 101 -vga virtio,clipboard=vnc`
C. Reboot the VM, and next time it opens in the console control bar (left side) you will see the clipboard icon that acts as the buffer/transfer. It allows you to paste into it from the host and then the VM will paste whatever you placed in there. Conversely, if you copy in the VM it will be placed in that "buffer" and then you can copy it on the host.




### **References:**
List any external references, guidelines, or documents that support this SOP.
- 
- 
- [https://benheater.com/proxmox-laptop-cybersecurity-lab/](https://benheater.com/proxmox-laptop-cybersecurity-lab/)

### **Revision History:**
- **Version 1.0** [Date]: [Brief description of changes]
- [Subsequent versions with dates and changes]