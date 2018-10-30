# Make boxplot with seaborn
bplot = sns.boxplot(x="Type", y="msprice", data=df1, width = 0.5, palette = 'colorblind', whis =1.5) #For outlier detection
# add stripplot to boxplot with Seaborn
bplot = sns.swarmplot(y='msprice', x ='Type', data = df1, color='black', alpha = 0.75)

bplot.axes.set_title("Minimum Support Price vs Type of Crop",
                            fontsize=16)
 
bplot.set_xlabel("Type of Crop", 
                        fontsize=14)
 
bplot.set_ylabel("Minimum Support Price",
                        fontsize=14)
 
bplot.tick_params(labelsize=10)
