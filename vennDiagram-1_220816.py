import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import venn

labels= venn.get_labels([range(10), range(5, 15)], fill=['number', 'logic'])
fig, ax = venn.venn2(labels, names=['list 1', 'list 2'])
fig.savefig('plactice.png', bbox_inches='tight')
plt.close()