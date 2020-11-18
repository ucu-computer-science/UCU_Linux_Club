### Week 5 File Systems Homework

### You should use this doc as a template, fork the repository, answer the questions and send us the link to grade.

### Try to answer these questions yourself, without consulting Google too much. Once you are finished with answering these questions however, read more on all the concepts you do not understand well, and reread our presentation on the topic

---

1. Using only command-line programs (`ls`, `cd`) jump around your user directories. **What are some of the interesting options for these programs?** ls: -l -a -la, cd: ???. 

1. Consider an i-node that contains 10 direct addresses to disk blocks. Disk Blocks are 1024 kb each. **What's the largest file size possible?** 10240 kb.

1. **How are external devices represented in file systems in Unix-like systems?** These devices' file systems are linked to the Unix file system, when device is pluged in.

1. For a given class, the student records are stored in a file. The records are randomly accessed and updated. Assume that each student's record is of fixed size. **Which of the three allocation schemes (contiguous, linked and table/indexed) should be used?** Contiguous.

1. One way to use contiguous allocation of the disk and not suffer from holes is to compact the disk every time a file is removed. Since all files are contiguous, copying a file requires a seek, a disk hand rotation, followed by the transfer at full speed. Writing the file back requires the same work. **Assuming a seek time of 5 msec, a rotational delay of 4 msec, a transfer rate of 80 MB/sec, an average file size of 8 KB, how long does it take to read a file into main memory and then write it back to the disk at a new location? Using these numbers, how long would it take to compact half of a 16-GB disk?** 201.8 sec.

1. **Suggest a few real-world examples for devices that would work with contiguous file systems?** An archive for history documents, library sorting book system, paper database of company's employers.

1. **Is it possible to recover the disk in the case that free space list is damaged?** Yes

1. **How many disk operations are necessary to get the file at `/home/$USER/Documents/history/foucault.txt` path?** Presume that we are located at the root (`/`), no i-node is cached and each i-node transition takes 1 disk operation. 5

smth edited

1. In many \*nix systems, the i-nodes are kept at the start of the disk. An alternative design is to allocate an i-node when a file is created and put the i-node at the start of the first block of the file. **What are the tradeoffs of this approach?** When user adresses to a file, system needs the i-node to read that file. To reach the fragment of memory (in which i-node stored) system should perform n operations. However, if i-node is stored at the very start, there's no need to seek for it. So, this approach shortens the time for reaching i-node(and, then, reading file). 
