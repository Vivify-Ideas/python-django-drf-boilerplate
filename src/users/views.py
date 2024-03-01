
from functools import partial
from urllib import request
from uuid import UUID
from django.http import JsonResponse
from rest_framework import viewsets, mixins,generics
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from traitlets import Instance
from yaml import serialize
from src.users import permissions
from src.users.models import User,Analysis
from src.users.permissions import Createanalysis, IFUserisAnalyst, IsUserOrReadOnly
from src.users.serializers import AnalysisSerializer, CreateUserSerializer, SubscribeAnalists, UserSerializer


class UserViewSet(mixins.RetrieveModelMixin,mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet,):
    """
    Creates, Updates and Retrieves - User 
    """

    queryset = User.objects.all()
    serializers = {'update_subscribe_analyst': SubscribeAnalists,'default': UserSerializer, 'create': CreateUserSerializer,}
    permissions = {'default': (IsUserOrReadOnly,), 'create': (AllowAny,)}

    

    def get_serializer_class(self):
        
        return self.serializers.get(self.action, self.serializers['default']) #--if seri class is not found it goes to default class

    def get_permissions(self):
        self.permission_classes = self.permissions.get(self.action, self.permissions['default'])
        return super().get_permissions()

    @action(detail=False, methods=['get'], url_path='me', url_name='me')
    def get_user_data(self, instance):
        try:
            return Response(UserSerializer(self.request.user, context={'request': self.request}).data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Wrong auth token' + e}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False,methods=['get'],url_path='my_analyst',url_name='my_analyst')
    def my_analyst(self,request,pk=None):
        try:
            user = User.objects.filter(pk=request.user.id).values('subscribe_analysts')
            user_serializer = UserSerializer(user)

            return Response(user)
        except Exception as e:
            return Response({
                "Message":"Not Found"
            })
    
    @action(detail=False, methods=['patch'])
    def update_subscribe_analyst(self, request, pk=None):
        user = User.objects.get(pk = request.user.id)
        serializer = SubscribeAnalists(user, data=request.data, partial = True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    
    
    

        
    


class AnalysisView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet, generics.CreateAPIView, ):
    queryset = Analysis.objects.all()
    serializer_class = AnalysisSerializer
    # permissions = {'default': (IFUserisAnalyst,),'create':(Createanalysis)}
    permissions = {'default':(IFUserisAnalyst,),'create':(Createanalysis,),}
    
    def get_permissions(self):
        self.permission_classes = self.permissions.get(self.action, self.permissions['default'])
        return super().get_permissions()

    
    
      
    def perform_create(self, serializer):
        
        analysis = serializer.save(analyst_user = self.request.user)
        
        # Update the is_analyst field of the respective user
        user_id = analysis.analyst_user_id
        try:
            user = User.objects.get(id=user_id)
            
            user.save()
        except User.DoesNotExist:
            # Handle case where user does not exist
            pass

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    


    # def get_object(self):
    #     # Customize this method to retrieve the object based on your specific logic
    #     # For example, you could retrieve the object based on a slug field instead of the primary key
    #     # For demonstration purposes, let's assume you want to retrieve the object based on a slug field
    #     slug = self.kwargs.get('analyst_user_id')
    #     # Perform your custom logic to retrieve the object
    #     queryset = Analysis.objects.filter(analyst_user_id=slug)
    #     # You can perform additional checks here, such as permission checks
    #     return queryset
    
    def retrieve(self, request, *args, **kwargs):
        get_param = self.request.query_params.get('id',None)
        # email = self.request.query_params.get('email', None)
        
        # get_param = self.kwargs.get('id')
        uid  = self.request.GET.get('id')
        print(uid)
        print('Hello')
        analysis = Analysis.objects.filter(analyst_user_id = get_param)
        serializer = AnalysisSerializer(analysis, many = True)
        return Response(serializer.data)

    
        
        


    
    

    
    

    

    
   
    
    
