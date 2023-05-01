## [Netcraft](https://www.netcraft.com/)
- Offer us information about the servers withouth evern intereacting with them
## [waybackurls](https://github.com/tomnomnom/waybackurls)
```bash
go install github.com/tomnomnom/waybackurls@latest
```

- To get a list of crawled URLs from a domain with the date it was obtained, we can add the `-dates` switch to our command as follows:
```bash 
waybackurls -dates https://facebook.com > waybackurls.txt
```
