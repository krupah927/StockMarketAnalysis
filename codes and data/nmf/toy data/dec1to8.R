
dec1to8<-as.matrix(amudec1to8)

row.names(dec1to8) <- dec1to8names$name

print(row.names)
dec1to8plot<-nmf(dec1to8, 9, "lee")

plot(dec1to8plot)

layout(cbind(1,2))
basismap(dec1to8plot, Rowv = TRUE, main = "NMF Clustering for Dec 1 to Dec 8")
hclustf
#coefmap(dec1to8plot)
fit(dec1to8plot)
summary(fit)
