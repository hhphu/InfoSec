- Used to transfer files between linux systems.
- Default configuration
```
cat /etc/exports
```

| Options | Description |
| --------- | ------------ |
| rw | Read and Write permissions |
| ro | Read Only permission |
| sync | Sycnrhonous data transfer (slower) |
| async | Asynchronous data transfer (faster) |
| secure | Ports above 1024 will not be used |
| insecure | Prots above 1024 will be used |
| no_subtree_check | This option disables the checking of subdirectory trees. |
| root_squash | Assigns all permissions to files of root UID/GID 0 to the UID/GID of anonymous, which prevents root from accessing files on an NFS mount |

## ExportFS
- Share the folder /mnt/nfs to the subnet `10.129.14.0/24` subnet so any host within the network can have access to it.
```shell
echo '/mnt/nfs 10.129.14.0/24(sync,no_subtree_check)' >> /etc/exports
systemctl restart nfs-kernel-server
exportfs
```

## Dangerous  Settings
- rw
- insecure
- nohide
- no_root_squash
- Since the first 1024 ports is used by root, if `insecure` is set, attackers can used ports above 1024

## Enumerate the service
- nmap
```shell
sudo nmap $IP -p111,2049 -sV -sC
	OR
sudo nmap --script nfs* $IP -sV -p111,2049
```

- Show available NFS shares
```shell
showmount -e $IP
```

- Mount NFS Share
```shell
mkdir target-NFS
sudo mount -t nfs $IP:/ ./target-NFS -o nolock
cd target-NFS
tree .
```

- List Contents with usernames & group names
```shell
ls -l mnt/nfs/
```

- List contents with UIDs & GUIDs
```shell
ls -n mnt/nfs/
```

-  Unmounting
```shell
sudo unmount ./target-NFS
```

