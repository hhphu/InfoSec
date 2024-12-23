# Attacking S3 Error

## Description: 
- When trying the exercise in Task 8, pilfering tihe iamge, I get a permission error that prevents me from calling create-restore-image-task.
- **Room:** AWS S3 - Attack and Defense
- **Task 8:** Lab: S3 - Abusing the Substrate
- **Step to reproduce:**
  1. Dump all the content of the s3 bucket to the local attack box machine using `aws s3 sync s3://assets.bestcloudcompany.org . --no-sign-request`
  2. Configure AWS with the provided credentials from THM 
  3. Run the command to perform **CreateRestoreImageTask**: `aws ec2 create-restore-image-task --object-key ami-056a6742115906e8c.bin --bucket assets.bestcloudcompany.org --name BCC`
- **Expected behavior:** I should be able to execute the command successfully without any error.
- **Actucal behavior:** I got an error message stating that the user is not authroized to perform this operation.
- **Error Message:**
  
```bash
An error occurred (UnauthorizedOperation) when calling the CreateRestoreImageTask operation: You are not authorized to perform this operation. User: arn:aws:iam::637423357278:user/637423357278 is not authorized to perform: ec2:CreateRestoreImageTask on resource: arn:aws:ec2:us-east-1::image/* because no identity-based policy allows the ec2:CreateRestoreImageTask action. Encoded authorization failure message: r-q1FTdq2ikQmsDLp33WjWJNoAE3NGvk4RfhpmNWKe2wPs5fTgaE3nh2pNu020kp0H03vSxw2c4k46R4w2yGEsH_H-X8XS26PljeUYUpSLj42-l3sfOsyZiKegil9PaFsQke9fy8Sg1o8mSmoQSPXWUv_eOvhLsxpfsJVLq82ZyHCghg0S6Ae1p2UXeS5GlDNFiwJ-YK8-e9kSLofdf10Qpercpd32HISlDudFrYC467wrQv7UchMxiVrSCUR4r_BFxOzfRunL8qRw4tc0kJug2iFebYJ9MZflHYAMDFqk3OnBKhqa2H7d26-a2JTFpPHwxsADBJYdcHB9fUct2zwii6vX8iU6BlJvKbxITmE7Awf5ivrpxKzNiiLuzpydJUaJ8ltbqfyxZzI7wIqy9DNezZ_SkYOx5z2Vc2FNwbLiyCFRWkpwj5dwRD--abXfqlD30v1GMFE5HiCr0h6d6alZUFoMCqQaFQSsyzo3LS3x8GsI_BZxK65Ji4HQX3G3C9R9NfakujqYIsFrf794I
```

- **Screenshot:**
![Screenshot 2024-12-23 015557](https://github.com/user-attachments/assets/86a99e13-2739-412c-ab99-af8d0cf50615)
