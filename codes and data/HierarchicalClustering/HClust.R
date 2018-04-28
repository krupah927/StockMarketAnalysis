#import data and assign 
RawData<-DEC6

#set rownames as 1st column so that the leaf at the dendrogram contains stock name
row.names(RawData) <- RawData$name


#-----------------------------------------------------------------


# define dendrogram object 
# "ave" - shows average linkage 
hc <- hclust(dist(RawData[,2:11]),"ave")
dend <- as.dendrogram(hc)
#to color the dendogram
#define number of colors 
library(dendextend)
par(mfrow = c(1,2), mar = c(3,1,4))
dend <- dend %>%
  color_branches(k = 3) %>%
  
  set("branches_lwd", c(2,1,2)) %>%
  set("branches_lty", c(1,2,1))
#plot dendrogram
plot(dend,main = "Hierarchical clustering (DEC6)")
#cut the tree to get groups ---- 3 is the number of clusters or 3 groups
clusterCut <- cutree(hc, 3)
plot(clusterCut)
#print all clusters
print(clusterCut)

#-------------------------------------------------------------

library(dendextend)
#library to get circular dendrogram
library(circlize)

# create a dendrogram
hc <- hclust(dist(RawData[,2:4]), "ave")
dend <- as.dendrogram(hc)

# modify the dendrogram to have some colors in the branches and labels
dend <- dend %>% 
  color_branches(k=3) %>% 
  color_labels(k=3)

# plot the radial plot
par(mar = rep(0,4)) 
# circlize_dendrogram(dend, dend_track_height = 0.8) 
circlize_dendrogram(dend, labels_track_height = NA, dend_track_height = .3) 

