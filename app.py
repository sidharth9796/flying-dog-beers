import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import os
from random import randrange
df_metrics = pd.read_csv('/home/drive/neuralcoref/bert_spacy_metrics.csv')
df_count=pd.read_csv('/home/drive/neuralcoref/entity_count.csv')

df_1 = pd.read_csv('/home/drive/neuralcoref/entity_count.csv')
df_2 = pd.read_csv('/home/drive/neuralcoref/data_new.csv')

df_model=pd.read_csv('/home/drive/neuralcoref/datarecords.csv')
#df_summary=pd.read_csv('model_summary.csv')

external_stylesheets=[
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    {   'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'},
         dbc.themes.BOOTSTRAP  ]

app = dash.Dash(__name__,external_stylesheets=external_stylesheets,suppress_callback_exceptions = True)
server = app.server

model_summary_dataset= html.Div( [
        dbc.Card( [
                #dbc.CardImg(src="logo.png", top=True),
                dbc.CardBody(
                [   html.Div([
                    html.H2(children="MODEL SUMMARY BASED ON RECORDS", style={"margin-left": "4%",'fontSize':'2.5rem',"font-weight":"bold",'font-family':'Trocchi, serif','color':'rgb(0,0,128)'}, className="card-title"),
                    dbc.FormGroup([
                            dbc.Label("Metrics",style={'fontSize':'2rem'},),
                            dbc.Checklist(
                                options=[
                                    {"label": "Precision", "value":'Precision'},
                                    {"label": "Recall", "value":'Recall'},
                                    {"label": "F1", "value":'F1'}
                                ],
                                value=[],
                                id="switches-inline-input-model-metrics-summary_modal_2",
                                style={'height': '300%', 'width': '100%','fontSize':'1.7rem'},
                                inline=True,
                                switch=True,
                            ),
                        ]
                    ),

                    html.Div([
                        html.Div([
                          html.P(
 children="Select Records",style={"margin-left": "0%",'fontSize':'1.5rem',"font-weight":"bold","margin-left": "4%",'font-family':'Trocchi, serif','color':'rgb(47,79,79)'},className="card-title"),
                        dcc.Dropdown( id="switches-inline-input-dataset-summary-front_modal_2",
                                      options=[{
                                                'label':i,
                                                'value':i}for i in df_model['TOTAL RECORDS'].unique()],
                                    placeholder="Select DATASET - first",
                                    style={'height': '300%', 'width': '100%','fontSize':'1.7rem',"margin-left": "2%"},
                                    value=[] )  ] ,className='six columns' )  ,

                        html.Div([
                            html.P(
                     children="Select Model ",style={"margin-left": "0%",'fontSize':'1.5rem',"font-weight":"bold" , 'font-family':'Trocchi, serif','color':'rgb(47,79,79)'},className="card-title"),
                            dcc.Dropdown( id="switches-inline-input-modal-summary-front_modal_2",
                                          options=[{
                                          'label':i,
                                           'value':i}for i in df_model['MODEL'].unique()],
                                         placeholder="Select MODEL - second",
                                         style={'height': '300%', 'width': '100%','fontSize':'1.7rem'},
                                         multi = True,
                                         value=['BERT','SPACY'] )
                                            ], className='six columns')
                                                      ]  , className="row" ) ,
                                            dcc.Graph(id='model_summary_dataset-front_modal_2',animate=True, style={"backgroundColor": "#1a2d46",'color':'#ffffff','width':"110rem","height":"100rem"} ) ]) ]) ]) ])



DropdownApp_entity = html.Div([
    html.H1(children='Evaluation metrics',style={"margin-left":"4%",'fontSize':'3.0rem','font-family': 'Trocchi, serif','color':'blue'}),
    dcc.Dropdown(id="entity_dropdown_modal_1",
                options=[{
                        'label': i,
                        'value': i}for i in df_metrics['Entity'].unique()],
                        placeholder="Select entity",
                        style={'height': '300%', 'width': '100%','fontSize':'1.7rem'},
                        multi = True,
                        value=[]),
    dcc.Dropdown(id="model_dropdown_modal_1",
                 options=[{
                    'label':i,
                    'value':i}for i in df_metrics['MODEL'].unique()],
                    placeholder="Select MODEL",
                style={'height': '300%', 'width': '100%'},
                    ),
    dbc.FormGroup([
            dbc.Label("Toggle Metrics",style={'fontSize':'2rem'}),
            dbc.Checklist(
                options=[
                    {"label": "Precision", "value": 'Precision'},
                    {"label": "Recall", "value":  'Recall'},
                    {"label": "F1", "value": 'F1'}
                ],
                value=["Precision","Recall","F1"],
                id="switches-inline-input-modal_1",
                inline=True,
                switch=True,
            ),
        ]
    )  ,
dcc.Graph(id='entity_graph_modal_1',animate=True,style={"backgroundColor": "#1a2d46",'color':'#ffffff','width':"110rem","height":"100rem"} ) ]  )

DropdownApp_model_term=  html.Div([
                  dbc.Card(
                       [
            #dbc.CardImg(src="logo.png", top=True),
            dbc.CardBody(
                [   html.Div([
                    html.H2(children="ENTITY SUMMARY", style={"margin-left": "4%",'fontSize':'2.5rem','font-family':'Trocchi, serif','color':'blue'}, className="card-title"),

                          html.P(
                          children="Select Records",style={"margin-left": "0%",'fontSize':'2.5rem',"font-weight":"bold","margin-left": "0%",'font-family':'Trocchi, serif','color':'rgb(47,79,79)'},className="card-title"),
                        dcc.Dropdown( id="entity-term-input-dataset-summary-front_modal_3",
                                      options=[{
                                                'label':i,
                                                'value':i}for i in df_model['TOTAL RECORDS'].unique()],
                                    placeholder="Select DATASET - first",
                                    style={'height': '300%', 'width': '98%','fontSize':'1.7rem',"margin-left": "0%"},
                                    value=[] )    ,
                        dcc.Graph(id='dcc_entity_bottom_left_modal_3',animate=True, style={"backgroundColor": "#1a2d46",'color':'#ffffff','width':"110rem","height":"100rem"} )

                                                   ]),

        ])  ]) ])


app.layout = html.Div(
    html.Div([
        html.Div(
            [  html.H1(children='Model Training Viewer',style={"margin-left": "10%",'fontSize':'4.5rem', 'font-family': 'Trocchi, serif' ,'color':'blue'},
                        className='six columns'),

            ], className="row",style={"margin": "38px 40px"}
        ),
        html.Div([
              html.Div([


            html.Div(
            [
                dbc.Card(
                        [
                        #dbc.CardImg(src="logo.png", top=True),
                    dbc.CardBody(
                        [   html.Div([
                            html.H2(children="BERT/SPACY METRICS ANALYSIS", style={"margin-left": "%",'fontSize':'2.5rem','font-family':'Trocchi, serif','color':'blue',},className="card-title"),
                            dcc.Dropdown(id="entity_dropdown_front",
                                                    options=[{
                                                            'label':i,
                                                            'value':i}for i in df_metrics['Entity'].unique()],
                                                                        placeholder="Select entity",
                                                        style={'height': '300%', 'width': '100%'},
                                                        multi = True,
                                                        value=[] ),

            html.Div([
                        html.Div([
                            dcc.Dropdown(id="model_dropdown_front",
                                                    options=[{
                                                            'label':i,
                                                            'value':i}for i in df_metrics['MODEL'].unique()],
                                                                        placeholder="Select MODEL",
                                                        style={'height': '300%', 'width': '100%'},
                                                        #value='BERT',
                                                    #    clearable=False

                                                       ) ] , className='six columns'                          ),

                            html.Div([
                            html.P(
                                children="Hint : clear the values",style={"margin-left": "0%",'fontSize':'1.5rem','color':'blue'},
                                    className="six columns",
                                                        )  ] , className='six columns'    )    ], className="row",style={"margin": "10px 0px 0px 0px"})   ,


                            dbc.FormGroup([
                                    dbc.Label("Metrics",style={'fontSize':'2rem'},),
                                    dbc.Checklist(
                                        options=[
                                            {"label": "Precision", "value":'Precision'},
                                            {"label": "Recall", "value":'Recall'},
                                            {"label": "F1", "value":'F1'}
                                        ],
                                        value=["Precision","Recall","F1"],
                                        id="switches-inline-input",
                                        style={'height': '300%', 'width': '100%','fontSize':'1.7rem'},
                                        inline=True,
                                        switch=True,
                                    ),
                                ]
                            ),
                            dcc.Graph(id='entity_graph_front',animate=True, style={'width': '100%'})  ,

                            html.P(
                                children="ENTITIES - Precision, F1, Recall scores ",style={"margin-left": "4%",'fontSize':'1.5rem','color':'blue'},
                                className="card-text",
                            ),
                            dbc.Button("Open App", id="openone",  color='warning', style={'margin': 'auto', 'width': '100%'}),
                            dbc.Modal(
                                [
                                    dbc.ModalBody(DropdownApp_entity),
                                    dbc.ModalFooter(
                                        dbc.Button("Close", id="closeone", className="ml-auto",outline=True,color="danger",block=True)
                                    ),
                                ],
                                id="modalone",size="xl"
                            ),
                        ]
                    ),
                ],
                style={"width": "134rem","height":"75rem",'background-color':'rgb(176,196,222)'},
            )
     ],className='nine columns')       ], className="row",  style={"margin": "38px 40px"}  ) ,

#card 2
            html.Div(
            [
                dbc.Card(
                        [
                        #dbc.CardImg(src="logo.png", top=True),
                dbc.CardBody(
                [   html.Div([
                    html.H2(children="MODEL SUMMARY BASED ON RECORDS", style={"margin-left": "0%",'fontSize':'2.5rem',"font-weight":"bold",'font-family':'Trocchi, serif','color':'rgb(0,0,128)'}, className="card-title"),


                    dbc.FormGroup([
                            dbc.Label("Metrics",style={'fontSize':'2rem'},),
                            dbc.Checklist(
                                options=[
                                    {"label": "Precision", "value":'Precision'},
                                    {"label": "Recall", "value":'Recall'},
                                    {"label": "F1", "value":'F1'}
                                ],
                                value=[],
                                id="switches-inline-input-model-metrics-summary",
                                style={'height': '300%', 'width': '100%','fontSize':'1.7rem'},
                                inline=True,
                                switch=True,
                            ),
                        ]
                    ),

                    html.Div([
                        html.Div([
                          html.P(
 children="Select Records",style={"margin-left": "0%",'fontSize':'1.5rem',"font-weight":"bold","margin-left": "4%",'font-family':'Trocchi, serif','color':'rgb(47,79,79)'},className="card-title"),
                        dcc.Dropdown( id="switches-inline-input-dataset-summary-front",
                                      options=[{
                                                'label':i,
                                                'value':i}for i in df_model['TOTAL RECORDS'].unique()],
                                    placeholder="Select DATASET - first",
                                    style={'height': '300%', 'width': '100%','fontSize':'1.7rem',"margin-left": "1%"},
                                    value=[] )  ] ,className='six columns' )  ,

                        html.Div([
                            html.P(
                     children="Select Model ",style={"margin-left": "0%",'fontSize':'1.5rem',"font-weight":"bold" , 'font-family':'Trocchi, serif','color':'rgb(47,79,79)'},className="card-title"),
                            dcc.Dropdown( id="switches-inline-input-modal-summary-front",
                                          options=[{
                                          'label':i,
                                           'value':i}for i in df_model['MODEL'].unique()],
                                         placeholder="Select MODEL - second",
                                         style={'height': '300%', 'width': '100%','fontSize':'1.7rem'},
                                         multi = True,
                                         value=['BERT','SPACY'] )
                                            ], className='six columns')
                                                      ]  , className="row" ) ,
                                            dcc.Graph(id='model_summary_dataset-front',animate=True, style={'width': '100%','margin-top': '22px'} )
                                                        ] ),
                                            html.P(
                                            children="ENTITIES - Precision, F1, Recall scores ",style={"margin-left": "4%",'fontSize':'1.5rem','color':'blue'},
                                                className="card-text",
                                                                        ),
                                            dbc.Button("Open App", id="opentwo",  color='primary', style={'margin': '0px', 'width': '100%'}),
                                            dbc.Modal(
                                                [   dbc.ModalBody(model_summary_dataset),
                                                    dbc.ModalFooter(
                                                    dbc.Button("Close", id="closetwo", className="ml-auto",outline=True,color="danger",block=True)
                                                    ),
                                                ],
                                                id="modaltwo",size="xl"
                                            ),
                                        ],
            style={"width": "134rem","height":"75rem",'background-color':'rgb(176,196,222)'}
                                    ),
     ],className='nine columns')       ], className="row",  style={"margin": "38px 40px"}  )
     ,

#card 3
            html.Div(
            [
                dbc.Card(
                        [
                        #dbc.CardImg(src="logo.png", top=True),
            dbc.CardBody(
                [   html.Div([
                    html.H2(children="ENTITY SUMMARY", style={"margin-left": "0%",'fontSize':'2.5rem','font-family':'Trocchi, serif','color':'blue'}, className="card-title"),

                          html.P(
                          children="Select Records",style={"margin-left": "0%",'fontSize':'2.5rem',"font-weight":"bold","margin-left": "0%",'font-family':'Trocchi, serif','color':'rgb(47,79,79)'},className="card-title"),
                        dcc.Dropdown( id="entity-term-input-dataset-summary-front",
                                      options=[{
                                                'label':i,
                                                'value':i}for i in df_model['TOTAL RECORDS'].unique()],
                                    placeholder="Select DATASET - first",
                                    style={'height': '300%', 'width': '98%','fontSize':'1.7rem',"margin-left": "0%"},
                                    value=[] )    ,
                        dcc.Graph(id='dcc_entity_bottom_left',animate=True, style={'width': '100%','margin-top': '22px'} )

                                                   ]),
                    html.P(
                            children="Tag frequency ",style={"margin-left": "4%",'fontSize':'1.5rem','color':'blue'},
                            className="card-text",
                                                ),
                    dbc.Button("Open App", id="openthree",  color='warning', style={'margin': 'auto', 'width': '100%',}),
                    dbc.Modal(
                        [
                            dbc.ModalBody(DropdownApp_model_term),
                            dbc.ModalFooter(
                                dbc.Button("Close", id="closethree", className="ml-auto",outline=True,color="danger",block=True)
                            ),
                        ],
                        id="modalthree",size="xl"
                    ),
                ],
                style={"width": "134rem","height":"75rem",'background-color':'rgb(176,196,222)'}
            ),
     ],className='nine columns')       ], className="row",  style={"margin": "38px 40px"}  )



                ]) ], className='ten columns offset-by-one')],
), style={"background-color": "rgb(220,220,220)"})


colors_entity_term=['rgb(139,69,19)','rgb(72,61,139)','rgb(139,0,139)','rgb(47,79,79)','rgb(0,100,0)','rgb(255,69,0)','rgb(128,0,0)','rgb(255,255,0)','rgb(0,128,128)','rgb(255,140,0)','rgb(0,128,128)','rgb(188,143,143)']
colors_entity=[['rgb((70,130,180)','rgb(70,130,180)','rgb(0,191,255)','rgb(25,25,112)'],['rgb(0,128,0)','rgb(0,100,0)','rgb(46,139,87)','rgb(136,255,77)']]
colors=['rgb(100,149,237)','rgb(188,143,143)','rgb(244,164,96)','rgb(65,105,225)','rgb(255,140,0)','rgb(55, 83, 109)','rgb(135,206,250)','rgb(192,192,192)','rgb(245,222,179)','rgb(255,228,225)','rgb(128,128,128)','rgb(0,128,128)','rgb(152,251,152)','rgb(220,20,60)','rgb(107,142,35)','rgb(221,160,221)','rgb(244,164,96)','rgb(128,0,0)','rgb(250,250,210)','rgb(245,255,250)']
#CARD 1 BERT METRICS ANALYSIS
@app.callback(
    dash.dependencies.Output('entity_graph_front','figure'),
    [dash.dependencies.Input('entity_dropdown_front','value'),
    dash.dependencies.Input('model_dropdown_front','value'),
    dash.dependencies.Input('switches-inline-input','value'),
            ]   )

def update_figure(dropdown,model,toggle):
    print("the dropdown model is ")
    print(dropdown)
    print("the model is ")
    print(model)
    print("the toggle is")
    print(toggle)
    data_select=[]
    #metrics=['Precision','Recall','F1']
    model_df =df_metrics.groupby('MODEL')
    for n,df in model_df:
        if n == model:
            #print(min_df[i])df
            #g=df_model[df_model['TOTAL RECORDS'] == dataset]
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print(df)
            #x=g[g['Entity'] == value]['Total_Records']
            for j in toggle:
                for index,value in enumerate(dropdown):
                    data_select.append(go.Bar(x=df[df['Entity'] == value]['Total_Records'],y=df[df['Entity'] == value][j],text=("{0} {1} {2}".format(value,j,model)),name=("{0} {1}".format(value,j)),textposition='auto',marker=dict(color = colors[index] ,line=dict(color='rgb(8,48,107)'))))
    print("-----------------------------------------------------")

    figure=dict(
                    data=data_select,
                    layout=go.Layout(title='EVALUATION METRICS',
                                       colorway=["#EF963B", "#EF533B"],hovermode="closest",
                                        xaxis={'title': "RECORDS",
                                               'titlefont':{'color': 'black','size': 20},
                                               'tickfont':{'color': 'black','size': 20 } },
                                       yaxis={'title': "ACCURACY",
                                              'titlefont':{'color': 'black','size': 20},
                                              'tickfont':{'color': 'black','size': 20 } },
                                       legend={'x': 1, 'y':1 }
                                               )
                                          )
    print("the figure is")

    print(figure['data'])
    return figure



# modal card one - BERT METRICS ANALYSIS

@app.callback(
    dash.dependencies.Output('entity_graph_modal_1','figure'),
    [dash.dependencies.Input('entity_dropdown_modal_1','value'),
    dash.dependencies.Input('model_dropdown_modal_1','value'),
    dash.dependencies.Input('switches-inline-input-modal_1','value'),
            ]   )
def update_figure(dropdown_modal_1,model_modal_1,toggle_modal_1):
    data_select=[]
    #metrics=['Precision','Recall','F1']
    model_df =df_metrics.groupby('MODEL')
    for n,df in model_df:
        if n == model_modal_1:
            #print(min_df[i])df
            #g=df_model[df_model['TOTAL RECORDS'] == dataset]
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print(df)
            #x=g[g['Entity'] == value]['Total_Records']
            for j in toggle_modal_1:
                for index,value in enumerate(dropdown_modal_1):
                    data_select.append(go.Bar(x=df[df['Entity'] == value]['Total_Records'],y=df[df['Entity'] == value][j],text=("{0} {1}".format(value,j)),name=("{0} {1}".format(value,j)),textposition='auto',marker=dict(color = colors[index] ,line=dict(color='rgb(8,48,107)'))))
    print("-----------------------------------------------------")

    #print("-----------------------------------------------------")

    figure=dict(
                    data=data_select,
                    layout=go.Layout(title='EVALUATION METRICS',
                                       colorway=["#EF963B", "#EF533B"],hovermode="closest",
                                        xaxis={'title': "RECORDS",
                                               'titlefont':{'color': 'black','size': 20},
                                               'tickfont':{'color': 'black','size': 20 } },
                                       yaxis={'title': "ACCURACY",
                                              'titlefont':{'color': 'black','size': 20},
                                              'tickfont':{'color': 'black','size': 20 } },
                                       legend={'x': 1, 'y':1 }
                                               )
                                              )
    return figure



#Module one
@app.callback(
    dash.dependencies.Output("modalone", "is_open"),
    [dash.dependencies.Input("openone", "n_clicks"), dash.dependencies.Input("closeone", "n_clicks")],
    [dash.dependencies.State("modalone", "is_open")],
)
def toggle_modal(n1,n2,is_open):
    if n1 or n2:
        return not is_open
    return is_open

#CARD 2
@app.callback(
    dash.dependencies.Output('model_summary_dataset-front','figure'),
    [
    dash.dependencies.Input('switches-inline-input-model-metrics-summary','value'),
    dash.dependencies.Input('switches-inline-input-dataset-summary-front','value'),
    dash.dependencies.Input('switches-inline-input-modal-summary-front','value')
    ] )
def modelsummarydatasetfront(metrics,dataset,model):
    print("njnkbttttttttttttttttttttttttt")
    print(metrics)
    print("\n\n\n\n\n\n")
    #print(type(dropdown))
    print(dataset)
    data_select=[]
    #metrics=['Precision','Recall','F1']
    total_df =df_model.groupby('TOTAL RECORDS')
    for n,g in total_df:
        if n == dataset:
            #print(min_df[i])df
            r=randrange(10)
            #g=df_model[df_model['TOTAL RECORDS'] == dataset]
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print(g)
            color_index=0
            #x=g[g['Entity'] == value]['Total_Records']
            for j in metrics:
                color_index=color_index+1
                for index,value in enumerate(model):
                    data_select.append(go.Bar(x=g['TOTAL RECORDS'],y=g[g['MODEL'] == value][j],text=("{0}{1}".format(value,j)),name=("{0}{1}".format(value,j)),textposition='auto',marker=dict(color=colors_entity[index][color_index],line=dict(color='rgb(70,130,180)'))))

                    print("\n\nthe data select is \n")
                    print(data_select)

    figure=dict(
                            data=data_select,
                            layout=go.Layout(title='EVALUATION METRICS',
                                   colorway=["#EF963B", "#EF533B"],hovermode="closest",
                                    xaxis={'title': "Records",
                                           'titlefont':{'color': 'black','size': 20},
                                           'tickfont':{'color': 'black','size': 20 } },
                                   yaxis={'title': "ACCURACY",
                                          'titlefont':{'color': 'black','size': 20},
                                          'tickfont':{'color': 'black','size': 20 } },

                                           )
                                          )
    return figure

#CARD 2 MODAL 2
@app.callback(
    dash.dependencies.Output('model_summary_dataset-front_modal_2','figure'),
    [
    dash.dependencies.Input('switches-inline-input-model-metrics-summary_modal_2','value'),
    dash.dependencies.Input('switches-inline-input-dataset-summary-front_modal_2','value'),
    dash.dependencies.Input('switches-inline-input-modal-summary-front_modal_2','value')
    ] )
def modelsummarydatasetfront(metrics,dataset,model):
    print(metrics)
    print("\n\n\n\n\n\n")
    #print(type(dropdown))
    print(dataset)
    data_select=[]
    #metrics=['Precision','Recall','F1']
    total_df =df_model.groupby('TOTAL RECORDS')
    for n,g in total_df:
        if n == dataset:
            #print(min_df[i])df
            r=randrange(10)
            #g=df_model[df_model['TOTAL RECORDS'] == dataset]
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print(g)
            color_index=0
            #x=g[g['Entity'] == value]['Total_Records']
            for j in metrics:
                color_index=color_index+1
                for index,value in enumerate(model):
                    data_select.append(go.Bar(x=g['TOTAL RECORDS'],y=g[g['MODEL'] == value][j],text=("{0}{1}".format(value,j)),name=("{0}{1}".format(value,j)),textposition='auto',marker=dict(color=colors_entity[index][color_index],line=dict(color='rgb(70,130,180)'))))

                    print("\n\nthe data select is \n")
                    print(data_select)

    figure=dict(
                            data=data_select,
                            layout=go.Layout(title='EVALUATION METRICS',
                                   colorway=["#EF963B", "#EF533B"],hovermode="closest",
                                    xaxis={'title': "Records",
                                           'titlefont':{'color': 'black','size': 20},
                                           'tickfont':{'color': 'black','size': 20 } },
                                   yaxis={'title': "ACCURACY",
                                          'titlefont':{'color': 'black','size': 20},
                                          'tickfont':{'color': 'black','size': 20 } },

                                           )
                                          )
    return figure

#Module Two
@app.callback(
    dash.dependencies.Output("modaltwo","is_open"),
    [dash.dependencies.Input("opentwo","n_clicks"), dash.dependencies.Input("closetwo","n_clicks")],
    [dash.dependencies.State("modaltwo","is_open")],
)
def toggle_modal(n1,n2,is_open):
    if n1 or n2:
        return not is_open
    return is_open



#CARD 3 TAG FREQUENCY
@app.callback(
    dash.dependencies.Output('dcc_entity_bottom_left','figure'),
    [dash.dependencies.Input('entity-term-input-dataset-summary-front','value'),

            ]   )


def update_figure(dataset):
    data_select=[]
    r=randrange(11)
    df_2=df_1.groupby('TOTAL RECORDS')
    for n,g in df_2:
        if n == dataset:
            #print(min_df[i])df
            df=g[g['TOTAL RECORDS']==n]
            data_select.append(go.Bar(x=df['Entities'],y=df['#Count'] ,name=("{0}".format(df['#Count'])),textposition='auto',marker=dict(color = colors_entity_term[r] ,line=dict(color='rgb(8,48,107)'))))


    figure=dict(
                    data=data_select,
                    layout=go.Layout(title='EVALUATION METRICS',
                                       colorway=["#EF963B", "#EF533B"],hovermode="closest",
                                        xaxis={'title': "RECORDS",
                                               'titlefont':{'color': 'black','size': 20},
                                               'tickfont':{'color': 'black','size': 10 } },
                                       yaxis={'title': "ACCURACY",
                                              'titlefont':{'color': 'black','size': 20},
                                              'tickfont':{'color': 'black','size': 20 } },
                                       legend={'x': 1, 'y':1 }
                                               )
                                              )
    return figure


#CARD 3 TAG Frequency modal 3
@app.callback(
    dash.dependencies.Output('dcc_entity_bottom_left_modal_3','figure'),
    [dash.dependencies.Input('entity-term-input-dataset-summary-front_modal_3','value'),

            ]   )


def update_figure(dataset):
    data_select=[]
    r=randrange(11)
    df_2=df_1.groupby('TOTAL RECORDS')
    for n,g in df_2:
        if n == dataset:
            #print(min_df[i])df
            df=g[g['TOTAL RECORDS']==n]
            data_select.append(go.Bar(x=df['Entities'],y=df['#Count'] ,name=("{0}".format(df['#Count'])),textposition='auto',marker=dict(color = colors_entity_term[r] ,line=dict(color='rgb(8,48,107)'))))


    figure=dict(
                    data=data_select,
                    layout=go.Layout(title='EVALUATION METRICS',
                                       colorway=["#EF963B", "#EF533B"],hovermode="closest",
                                        xaxis={'title': "RECORDS",
                                               'titlefont':{'color': 'black','size': 20},
                                               'tickfont':{'color': 'black','size': 10 } },
                                       yaxis={'title': "ACCURACY",
                                              'titlefont':{'color': 'black','size': 20},
                                              'tickfont':{'color': 'black','size': 20 } },
                                       legend={'x': 1, 'y':1 }
                                               )
                                              )
    return figure


#Module Three
@app.callback(
    dash.dependencies.Output("modalthree","is_open"),
    [dash.dependencies.Input("openthree","n_clicks"), dash.dependencies.Input("closethree","n_clicks")],
    [dash.dependencies.State("modalthree","is_open")],
)
def toggle_modal(n1,n2,is_open):
    if n1 or n2:
        return not is_open
    return is_open


if __name__ == '__main__':
    app.run_server(debug=True)
