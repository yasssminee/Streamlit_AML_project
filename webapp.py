import streamlit as st 
from PIL import Image
# import requests


st.set_page_config(page_title="AI Risk: Hydatis" , page_icon="Papers\logo-Hydatis-sans-slogan.png" , layout="wide")


import streamlit as st


with st.container():
    st.subheader(" Realised by: Yassmine Selmi")
    linkedin_icon = st.image("linkedin.png", width=50)
    st.write("Contact Me! [Yassmine](https://www.linkedin.com/in/yassmine-selmi-1b3652208/)")
    linkedin_container = st.empty()

    linkedin_icon = st.image("logo-Hydatis-sans-slogan.png", width=200)
    st.write("Visit Hydatis Website! [Click here ! ](https://www.hydatis.com/)")

    st.title(" Hydatis Summer Internship: AI Risk ")
    st.subheader("The fight against money laundering using artificial Intelligence to enhance accurate detection of suspicious activities while reducing false positive alerts")
    
with st.container():
    st.write("---")
    st.title("Dataset Used")
    st.subheader("IBM Transactions for Anti Money Laundering (AML)")
    image_column1 , text_column= st.columns((2,1))
    with image_column1:
        image = Image.open('AML-Data.png')
        st.image(image, caption='IBM Dataset')
    with text_column:
        st.subheader("""
                    We release 6 datasets here divided into two groups of three:

                    . Group HI has a relatively higher illicit ratio (more laundering).
                    . Group LI has a relatively lower illicit ratio (less laundering).
                    
                    Both HI and LI internally have three sets of data: small, medium, and large.
                    Finally, we provide two files for each of the six datasets:
                    
                    A. A list of transactions in CSV format
                    
                    B. A text file list of laundering transactions following one of 8 particular patterns introduced by Suzumura and Kanezashi in their AMLSim simulator.

                     """)
        
        st.write("More details about the Dataset [Click here ! ](https://www.kaggle.com/datasets/ealtman2019/ibm-transactions-for-anti-money-laundering-aml)")
        
    
    


with st.container():
    st.write("---")
    st.title("Work overflow")
    st.write("The diagram below provides an overview of our comprehensive methodology, which involves two distinct databases: one containing 5 million transaction records, and the other featuring examples of money laundering scenarios encompassing eight distinct types. Our project comprises five key stages:")
    image = Image.open('diagram.png')
    st.image(image, caption='Summarisation of the work achieved')
    st.subheader("1/ Preprocessing")
    st.write("This initial step involves data preparation and cleaning.")
    
    st.subheader("2/ Graph Construction")
    st.write("We transform the transaction dataset into a substantial graph, comprising 515,088 nodes and 5,078,345 edges. The scenarios dataset is converted into multiple smaller graphs, each representing a unique money laundering scenario.")
    
    st.subheader("3/ Subgraph Extraction")
    st.write("Utilizing algorithmic techniques, we extract subgraphs from the significant graph that exhibit similarity to our labeled scenario graphs dataset.")
    st.subheader("4/ Training a Graph Neural Network (GNN) on Labeled Graphs (Classification)")
    st.write("A Graph Neural Network (GNN) is trained on the labeled graphs, facilitating classification tasks.")
    
    st.subheader("5/ Classifying Extracted Subgraphs and Calculating Similarity")
    st.write("The GNN classifies the extracted subgraphs. Subsequently, we calculate the similarity between the classified extracted subgraphs and the labeled graphs present in our dataset, utilizing graph-based metrics.")
    
with st.container():
    st.write("---")
    st.title("Results")
    
    st.title("1. Customized Graph Neural Network model:")
    
    code = st.text_area("""
                        
class GNN(torch.nn.Module):
                        
    def __init__(self, input_size, hidden_channels, num_classes):
        super(GNN, self).__init__()
        self.conv1 = GCNConv(input_size, hidden_channels)
        self.conv2 = GCNConv(hidden_channels, hidden_channels)
        self.conv3 = GCNConv(hidden_channels, hidden_channels)
        self.conv4 = GCNConv(hidden_channels, hidden_channels)

        self.hidden_layer = Linear(hidden_channels, hidden_channels)

        self.lin = Linear(hidden_channels, num_classes)  # takes the learned features from the GNN layers and maps them to class scores

    def forward(self, x, edge_index, batch):
        x = self.conv1(x, edge_index)
        x = F.relu(x)
        x = self.conv2(x, edge_index)
        x = F.relu(x)

        x = self.conv3(x, edge_index)
        x = F.relu(x)
        x = self.conv4(x, edge_index) # adding a 4th GConLayer

        x = global_mean_pool(x, batch)
        x = F.relu(x)
        x = F.dropout(x, training=self.training)
        x = self.lin(x)
        return x""")

    st.subheader("GNN performance")
    st.write("Test Accuracy: 0.8136")
    st.write("Number of Confidence Scores Under 0.9: 1874")
    st.write("Minimum score of correct classifications 0.3918802738189697")
    st.write("~ 10% of correct classified scenarios showing a confidence score under 0.9")
    st.write("Percentage of correct classified score under 0.9 : 11.3803 %")
    
    
    st.title("2. Comparison between Existed scenarios and Extracted ones: ")
    st.write("Samples of existed scenarios in the Dataset")
    
    image_column1 , image_column2 , text_column= st.columns((1,1,2))
    with image_column1:
        image = Image.open('sg_scenario1.png')
        st.image(image)
    with image_column2:
        image = Image.open('sg_scenario2.png')
        st.image(image)
    
    with text_column:
        st.subheader("Existed Scatter-Gather Scenarios")
        st.write("Scatter-Gather is when an account A do many transactions to an account B through multiple accounts") 
        st.write("Illustration :") 
        st.write("A --> U --> B")
        st.write("A --> E --> B")
        st.write("A --> Y --> B")
        st.write("A --> N --> B")
    
    st.write("Samples of Extracted scenarios using an algorithmic solution")
    image_column1 , image_column2 , text_column= st.columns((1,1,2))
    with image_column1:
        image = Image.open('sg_predected.png')
        st.image(image)
    with image_column2:
        image = Image.open('sg_predected2.png')
        st.image(image)
    
    with text_column:
        st.subheader("Predected Scatter-Gather Scenarios")
        st.write(" Using an algorithmic solution, i was able to extract scenarios with 90% similarity with the existed scenarios ")
    
    st.title("3. GNN Classification and confident score ")
    st.subheader(" Test on the first samlpe of extracted scenarios:")
    st.write("predicted class   ['SCATTER-GATHER']  and confidence score  tensor([0.9999]) ")
    
    
    
with st.container():
    
    st.write("---")
    st.header(" :mailbox: Get In Touch With Me ! ")
    st.write("##")
    
    contact_form="""
    <form action="https://formsubmit.co/yassmineselmi@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="You Name" required>
        <input type="email" name="email" placeholder="You Email" required>
        <textarea name="message" placeholder="Your Message Here ! "></textarea>
        <button type="submit">Send</button>
    </form>
    """
    
    st.markdown(contact_form , unsafe_allow_html=True)
    
    def local_css(file_name):
        with open(file_name) as f : 
            st.markdown(f"<style>{f.read()}</style>" , unsafe_allow_html=True)
    
    
    local_css("style/style.css")