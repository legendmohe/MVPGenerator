/*
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package {{package_name}}.presenters;

import {{package_name}}.mvp.presenters.MvpBasePresenter;
import {{package_name}}.views.{{view_name}};

/**
 * Created by {{author}} on {{create_time}}.
 */
public class {{presenter_name}} extends MvpBasePresenter<{{view_name}}> {
    protected static final String TAG = "{{presenter_name}}";

    public {{presenter_name}}({{view_name}} view) {
        super(view);
    }

    @Override
    public void start() {
        Log.d(TAG, "{{presenter_name}} start.");
    }

    @Override
    public void stop() {
        Log.d(TAG, "{{presenter_name}} stop.");
    }
}