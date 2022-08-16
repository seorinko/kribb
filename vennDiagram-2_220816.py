import matplotlib
import venn
labels = venn.get_labels([{1,2,3,4}, {2,3,5,6}, {1,6,3,9}, {7,4,9,11}], fill=['number'])
fig, ax = venn.venn4(labels, names=['A', 'B', 'C', 'D'])
fig.savefig('plactice-2.png')